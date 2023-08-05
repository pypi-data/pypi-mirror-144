"""Translation layer between pyproject config and setuptools distribution and
metadata objects.

The distribution and metadata objects are modeled after (an old version of)
core metadata, therefore configs in the format specified for ``pyproject.toml``
need to be processed before being applied.
"""
import logging
import os
from collections.abc import Mapping
from email.headerregistry import Address
from functools import partial
from itertools import chain
from types import MappingProxyType
from typing import (TYPE_CHECKING, Any, Callable, Dict, List, Optional, Set, Tuple,
                    Type, Union)

if TYPE_CHECKING:
    from setuptools._importlib import metadata  # noqa
    from setuptools.dist import Distribution  # noqa

EMPTY: Mapping = MappingProxyType({})  # Immutable dict-like
_Path = Union[os.PathLike, str]
_DictOrStr = Union[dict, str]
_CorrespFn = Callable[["Distribution", Any, _Path], None]
_Correspondence = Union[str, _CorrespFn]

_logger = logging.getLogger(__name__)


def apply(dist: "Distribution", config: dict, filename: _Path) -> "Distribution":
    """Apply configuration dict read with :func:`read_configuration`"""

    root_dir = os.path.dirname(filename) or "."
    tool_table = config.get("tool", {}).get("setuptools", {})
    project_table = config.get("project", {}).copy()
    _unify_entry_points(project_table)
    for field, value in project_table.items():
        norm_key = json_compatible_key(field)
        corresp = PYPROJECT_CORRESPONDENCE.get(norm_key, norm_key)
        if callable(corresp):
            corresp(dist, value, root_dir)
        else:
            _set_config(dist, corresp, value)

    for field, value in tool_table.items():
        norm_key = json_compatible_key(field)
        norm_key = TOOL_TABLE_RENAMES.get(norm_key, norm_key)
        _set_config(dist, norm_key, value)

    _copy_command_options(config, dist, filename)

    current_directory = os.getcwd()
    os.chdir(root_dir)
    try:
        dist._finalize_requires()
        dist._finalize_license_files()
    finally:
        os.chdir(current_directory)

    return dist


def json_compatible_key(key: str) -> str:
    """As defined in :pep:`566#json-compatible-metadata`"""
    return key.lower().replace("-", "_")


def _set_config(dist: "Distribution", field: str, value: Any):
    setter = getattr(dist.metadata, f"set_{field}", None)
    if setter:
        setter(value)
    elif hasattr(dist.metadata, field) or field in SETUPTOOLS_PATCHES:
        setattr(dist.metadata, field, value)
    else:
        setattr(dist, field, value)


_CONTENT_TYPES = {
    ".md": "text/markdown",
    ".rst": "text/x-rst",
    ".txt": "text/plain",
}


def _guess_content_type(file: str) -> Optional[str]:
    _, ext = os.path.splitext(file.lower())
    if not ext:
        return None

    if ext in _CONTENT_TYPES:
        return _CONTENT_TYPES[ext]

    valid = ", ".join(f"{k} ({v})" for k, v in _CONTENT_TYPES.items())
    msg = f"only the following file extensions are recognized: {valid}."
    raise ValueError(f"Undefined content type for {file}, {msg}")


def _long_description(dist: "Distribution", val: _DictOrStr, root_dir: _Path):
    from setuptools.config import expand

    if isinstance(val, str):
        text = expand.read_files(val, root_dir)
        ctype = _guess_content_type(val)
    else:
        text = val.get("text") or expand.read_files(val.get("file", []), root_dir)
        ctype = val["content-type"]

    _set_config(dist, "long_description", text)
    if ctype:
        _set_config(dist, "long_description_content_type", ctype)


def _license(dist: "Distribution", val: dict, root_dir: _Path):
    from setuptools.config import expand

    if "file" in val:
        _set_config(dist, "license", expand.read_files([val["file"]], root_dir))
    else:
        _set_config(dist, "license", val["text"])


def _people(dist: "Distribution", val: List[dict], _root_dir: _Path, kind: str):
    field = []
    email_field = []
    for person in val:
        if "name" not in person:
            email_field.append(person["email"])
        elif "email" not in person:
            field.append(person["name"])
        else:
            addr = Address(display_name=person["name"], addr_spec=person["email"])
            email_field.append(str(addr))

    if field:
        _set_config(dist, kind, ", ".join(field))
    if email_field:
        _set_config(dist, f"{kind}_email", ", ".join(email_field))


def _project_urls(dist: "Distribution", val: dict, _root_dir):
    special = {"downloadurl": "download_url", "homepage": "url"}
    for key, url in val.items():
        norm_key = json_compatible_key(key).replace("_", "")
        _set_config(dist, special.get(norm_key, key), url)
    # If `homepage` is missing, distutils will warn the following message:
    #     "warning: check: missing required meta-data: url"
    # In the context of PEP 621, users might ask themselves: "which url?".
    # Let's add a warning before distutils check to help users understand the problem:
    if not dist.metadata.url:
        msg = (
            "Missing `Homepage` url.\nIt is advisable to link some kind of reference "
            "for your project (e.g. source code or documentation).\n"
        )
        _logger.warning(msg)
    _set_config(dist, "project_urls", val.copy())


def _python_requires(dist: "Distribution", val: dict, _root_dir):
    from setuptools.extern.packaging.specifiers import SpecifierSet

    _set_config(dist, "python_requires", SpecifierSet(val))


def _unify_entry_points(project_table: dict):
    project = project_table
    entry_points = project.pop("entry-points", project.pop("entry_points", {}))
    renaming = {"scripts": "console_scripts", "gui_scripts": "gui_scripts"}
    for key, value in list(project.items()):  # eager to allow modifications
        norm_key = json_compatible_key(key)
        if norm_key in renaming and value:
            entry_points[renaming[norm_key]] = project.pop(key)

    if entry_points:
        project["entry-points"] = {
            name: [f"{k} = {v}" for k, v in group.items()]
            for name, group in entry_points.items()
        }


def _copy_command_options(pyproject: dict, dist: "Distribution", filename: _Path):
    tool_table = pyproject.get("tool", {})
    cmdclass = tool_table.get("setuptools", {}).get("cmdclass", {})
    valid_options = _valid_command_options(cmdclass)

    cmd_opts = dist.command_options
    for cmd, config in pyproject.get("tool", {}).get("distutils", {}).items():
        cmd = json_compatible_key(cmd)
        valid = valid_options.get(cmd, set())
        cmd_opts.setdefault(cmd, {})
        for key, value in config.items():
            key = json_compatible_key(key)
            cmd_opts[cmd][key] = (str(filename), value)
            if key not in valid:
                # To avoid removing options that are specified dynamically we
                # just log a warn...
                _logger.warning(f"Command option {cmd}.{key} is not defined")


def _valid_command_options(cmdclass: Mapping = EMPTY) -> Dict[str, Set[str]]:
    from .._importlib import metadata
    from setuptools.dist import Distribution

    valid_options = {"global": _normalise_cmd_options(Distribution.global_options)}

    unloaded_entry_points = metadata.entry_points(group='distutils.commands')
    loaded_entry_points = (_load_ep(ep) for ep in unloaded_entry_points)
    entry_points = (ep for ep in loaded_entry_points if ep)
    for cmd, cmd_class in chain(entry_points, cmdclass.items()):
        opts = valid_options.get(cmd, set())
        opts = opts | _normalise_cmd_options(getattr(cmd_class, "user_options", []))
        valid_options[cmd] = opts

    return valid_options


def _load_ep(ep: "metadata.EntryPoint") -> Optional[Tuple[str, Type]]:
    # Ignore all the errors
    try:
        return (ep.name, ep.load())
    except Exception as ex:
        msg = f"{ex.__class__.__name__} while trying to load entry-point {ep.name}"
        _logger.warning(f"{msg}: {ex}")
        return None


def _normalise_cmd_option_key(name: str) -> str:
    return json_compatible_key(name).strip("_=")


def _normalise_cmd_options(desc: List[Tuple[str, Optional[str], str]]) -> Set[str]:
    return {_normalise_cmd_option_key(fancy_option[0]) for fancy_option in desc}


PYPROJECT_CORRESPONDENCE: Dict[str, _Correspondence] = {
    "readme": _long_description,
    "license": _license,
    "authors": partial(_people, kind="author"),
    "maintainers": partial(_people, kind="maintainer"),
    "urls": _project_urls,
    "dependencies": "install_requires",
    "optional_dependencies": "extras_require",
    "requires_python": _python_requires,
}

TOOL_TABLE_RENAMES = {"script_files": "scripts"}

SETUPTOOLS_PATCHES = {"long_description_content_type", "project_urls",
                      "provides_extras", "license_file", "license_files"}
