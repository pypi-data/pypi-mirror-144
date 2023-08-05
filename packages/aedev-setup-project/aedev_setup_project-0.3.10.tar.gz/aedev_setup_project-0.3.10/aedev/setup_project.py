"""
project setup helper functions
==============================

this portion of the ``aedev`` namespace is providing constants and helper functions to install/setup Python projects of
applications, modules, packages, namespace portions and their root packages via the setuptools package.

the function :func:`project_env_vars` is analyzing a Python project and is providing the project properties as a dict of
project environment variable values.

the main goal of this project analysis is to:

   #. ease the setup process of Python projects,
   #. replace additional setup tools like e.g. `pipx` or `poetry` and
   #. eliminate or at least minimize redundancies of the project properties, stored in the project files like
      `setup.py`, `setup.cfg', `pyproject.toml`, ...

e.g. if you have to change the short description/title or the version number of a project you only need to edit them in
one single place of your project. after that, the changed project property value will be automatically propagated/used
in the next setup process.


basic helper functions
----------------------

while :func:`code_file_version` determines the current version of any type of Python code file, :func:`code_file_title`
does the same for the title of the code file's docstring.

package data resources of a project can be determined by calling the function :func:`find_package_data`. the return
value can directly be passed to the `package_data` item of the kwargs passed to `setuptools.setup`.

an optional namespace of a package gets determined and returned as string by the function :func:`namespace_guess`.


determine project environment variable values
---------------------------------------------

the function :func:`project_env_vars` inspects the folder of a Python project to generate a complete mapping of
environment variables representing project properties like e.g. names, ids, urls, file paths, versions or the content
of the readme file.

if the current working directory is the root directory of a Python project to analyze then it can be called without
specifying any arguments::

    pev = project_env_vars()

to analyze a project in any other directory specify the path in the :paramref:`~project_env_vars.project_path`
argument::

    pev = project_env_vars(project_path='path/to/project_or_parent')

the project property values can be retrieved from the returned dictionary (the ``pev`` variable) either via the function
:func:`pev_str` (only for string values), the function :func:`pev_val` or directly via getitem. the following example is
retrieving a string reflecting the name of the package::

    package_name = pev_str(pev, 'package_name')

the type of project gets mapped by the `'project_type'` key. recognized project types are e.g. :data:`a  module
<MODULE_PRJ>`, :data:`a package <PACKAGE_PRJ>`, :data:`a namespace root <ROOT_PRJ>`, or an
:data:`application <APP_PRJ>`.

if the current or specified directory to analyze is the parent directory of your projects (and is defined in
:data:`PARENT_FOLDERS`) then the mapped project type key will contain the special pseudo value :data:`PARENT_PRJ`,
which gets recognized by the :mod:`aedev.git_repo_manager` development tools e.g. for the creation of a new projects
and the bulk processing of multiple projects.

other useful properties in the `pev` mapping dictionary for real projects are e.g. `'package_version'` (determined e.g.
from the __version__ module variable), `'repo_root'` (the url prefix to the remote/origin repositories host), or
`'setup_kwargs'` (the keyword arguments passed to the `setuptools.setup` function).

.. hint::
    for a complete list of all available project environment variables check either the code of this module or the
    content of the returned `pev` variable (the latter can be done alternatively e.g. by running the
    :mod:`grm <aedev.git_repo_manager>` tool with the ``show-status`` command line argument).


configure project environment variable values
---------------------------------------------

the default values of project environment variables provided by this module are pre-set for the easy maintenance of the
namespaces `aedev <https://gitlab.com/aedev-group/projects>`__ and `ae <https://gitlab.com/ae-group/projects>`__.
e.g. the default value for the author name of the inspected project is the same as for this module, declared via the
module constant :data:`STK_AUTHOR`.

various alternative ways are provided to adapt the default value of an environment variable to your needs (listed in
the order of preference - the first has the highest priority, the last the lowest):

    #. add a config variable in the :data:`PEV_DEFAULTS_SECTION_NAME` section of your app.
    #. provide a :mod:`setup-hook module <aedev.setup_hook>`.
    #. specify `metadata` option values in the `setup.cfg` configuration file of your project.
    #. monkey-patch the value of a global constant of this module.


to overwrite the default value of a project environment variable via the app config variables add a section with the
name specified by the :data:`PEV_DEFAULTS_SECTION_NAME` constant in one of your app's config files. then add for each
variable to overwrite/adopt a config variable with the same (case-sensitive) name as the module constant or the project
environment variable. e.g. the following section example is setting/adapting the author name to `'My Author Name'`::

    [pevDefaults]
    STK_AUTHOR = 'My Author Name'

.. note::
    this way is only available for :class:`console <ae.console.ConsoleApp>` and :class:`gui <ae.gui_app.MainAppBase>`
    apps. to properly patch the project environment values, pass the instance of your app class into the call of
    :func:`project_env_vars` as the :paramref:`~project_env_vars.cae` argument.


if code has to be executed to calculate the final value of a project environment variable, then you can :mod:`provide a
setup hook file <aedev.setup_hook>`, named `setup_hook.py`, with the following content::

    def extend_project_env_vars(pev, path=""):
        author_name = determine_author_name(...)
        pev['STK_AUTHOR'] = author_name
        pev['setup_kwargs']['author'] = author_name

.. note::
    in contrary to the other alternatives, the author name has to be corrected in two project environment variables,
    because the setup hook gets called after all combined project environment variable values are fully initialized.
    additionally instead of :func:`project_env_vars` the function :func:`~aedev.setup_hook.hooked_project_env_vars` has
    to be called from within your projects `setup.py` file.


to configure/overwrite a setup_kwarg project environment variable or one of the ``STK_*`` module constants put them in a
project-specific `setup.cfg` file. for the author name use the `author` option of the `metadata` section in your
`setup.cfg` like so::

    [metadata]
    author = My Author Name


another alternative is to directly monkey patch the default value of a ``STK_*`` constant of this module before you call
the :func:`project_env_vars` function. e.g. to adapt the author name :data:`STK_AUTHOR` has to be patched::

    import aedev.setup_project

    aedev.setup_project.STK_AUTHOR = "My Author Name"
    pev = aedev.setup_project.project_env_vars(project_path=..., from_setup=True)

.. hint::
    if :func:`project_env_vars` gets called from within of your `setup.py` file, then the project path and a `True`
    argument has to be passed to the parameters :paramref:`~project_env_vars.project_path` and
    :paramref:`~project_env_vars.from_setup`. the project path can be determined via `os.path.dirname(__file__)`
    (assuming `setup.py` is situated in the project path root folder).

"""
import getpass
import glob
import os
import re

from distutils.errors import DistutilsFileError
from typing import Any, Dict, List, Optional, Sequence, Tuple, Union, cast

import setuptools
from setuptools.config import read_configuration

# import unreferenced vars (BUILD_CONFIG_FILE, DOCS_FOLDER, TEMPLATES_FOLDER, TESTS_FOLDER) to ensure for incomplete pev
# .. maps a non-empty default value if determined via pev_str().
# noinspection PyUnresolvedReferences
from ae.base import (                                       # type: ignore # noqa: F401 # pylint:disable=unused-import
    BUILD_CONFIG_FILE, DOCS_FOLDER, PACKAGE_INCLUDE_FILES_PREFIX, PY_EXT, PY_INIT, TEMPLATES_FOLDER, TESTS_FOLDER,
    import_module, in_wd, main_file_paths_parts, norm_path, project_main_file, read_file)


__version__ = '0.3.10'


APP_PRJ = 'app'                                             #: gui application project
MODULE_PRJ = 'module'                                       #: module portion/project
PACKAGE_PRJ = 'package'                                     #: package portion/project
PARENT_PRJ = 'projects-parent-dir'                          #: pseudo project type for new project started in parent-dir
ROOT_PRJ = 'namespace-root'                                 #: namespace root project
NO_PRJ = ''                                                 #: no project detected


DOCS_HOST_PROTOCOL = 'https://'                             #: documentation host connection protocol
DOCS_DOMAIN = 'readthedocs.io'                              #: documentation dns domain

PARENT_FOLDERS = (
    'Projects', 'PycharmProjects', 'esc', 'old_src', 'projects', 'repo', 'repos', 'source', 'src', getpass.getuser())
""" names of parent folders containing Python project directories """

PEV_DEFAULTS_SECTION_NAME = 'pevDefaults'                   #: main app config section with optional pev default values

PYPI_PROJECT_ROOT = "https://pypi.org/project"              #: PYPI projects root url

REPO_HOST_PROTOCOL = 'https://'                             #: repo host connection protocol
REPO_CODE_DOMAIN = 'gitlab.com'                             #: code repository dns domain (gitlab.com|github.com)
REPO_PAGES_DOMAIN = 'gitlab.io'                             #: repository pages internet/dns domain
REPO_GROUP_SUFFIX = '-group'                                #: repository users group name suffix

REQ_FILE_NAME = 'requirements.txt'                          #: requirements default file name
REQ_DEV_FILE_NAME = 'dev_requirements.txt'                  #: default file name for development/template requirements

# STK_* constants holding default values of supported setuptools setup() keyword arguments
STK_AUTHOR = "AndiEcker"                                    #: project author name default
STK_AUTHOR_EMAIL = "aecker2@gmail.com"                      #: project author email default
STK_LICENSE = "OSI Approved :: GNU General Public License v3 or later (GPLv3+)"     #: project license default
STK_CLASSIFIERS = [
            "Development Status :: 3 - Alpha",
            "License :: " + STK_LICENSE,
            "Natural Language :: English",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.6",
            "Topic :: Software Development :: Libraries :: Python Modules",
        ]                                                   #: project classifiers defaults
STK_KEYWORDS = [
            'configuration',
            'development',
            'environment',
            'productivity',
        ]
STK_PYTHON_REQUIRES = ">=3.6"                               #: default required Python version of project

VERSION_QUOTE = "'"                                         #: quote character of the __version__ number variable value
VERSION_PREFIX = "__version__ = " + VERSION_QUOTE           #: search string to find the __version__ variable


DataFilesType = List[Tuple[str, Tuple[str, ...]]]           #: setup_kwargs['data_files']
PackageDataType = Dict[str, List[str]]                      #: setup_kwargs['package_data']
SetupKwargsType = Dict[str, Any]                            #: setuptools.setup()-kwargs

PevVarType = Union[str, Sequence[str], DataFilesType, SetupKwargsType]
""" single project environment variable """
PevType = Dict[str, PevVarType]                                         #: project env vars mapping


# ------------- helpers for :func:`project_env_vars` --------------------------------------------------------------


def _compile_remote_vars(pev: PevType):
    package_name = pev_str(pev, 'package_name')
    package_prefix = pev_str(pev, 'namespace_name') or package_name

    pev['docs_root'] = docs_root = f"{pev_str(pev, 'DOCS_HOST_PROTOCOL')}{package_prefix}.{pev_str(pev, 'DOCS_DOMAIN')}"
    pev['docs_code'] = f"{docs_root}/en/latest/_modules/{pev_str(pev, 'import_name').replace('.', '/')}.html"
    pev['docs_url'] = f"{docs_root}/en/latest/_autosummary/{pev_str(pev, 'import_name')}.html"

    pev['repo_domain'] = repo_code_domain = pev_str(pev, 'REPO_CODE_DOMAIN')
    pev['repo_host'] = repo_host = f"{pev_str(pev, 'REPO_HOST_PROTOCOL')}{repo_code_domain}"
    pev['repo_group'] = repo_group = f"{package_prefix}{pev_str(pev, 'REPO_GROUP_SUFFIX')}"
    pev['repo_root'] = repo_root = f"{repo_host}/{repo_group}"

    pev['repo_pages'] = f"{pev_str(pev, 'REPO_HOST_PROTOCOL')}{repo_group}.{pev_str(pev, 'REPO_PAGES_DOMAIN')}"
    pev['repo_url'] = f"{repo_root}/{package_name}"

    pev['pypi_url'] = f"{pev_str(pev, 'PYPI_PROJECT_ROOT')}/{pev_str(pev, 'pip_name')}"


def _compile_setup_kwargs(pev: PevType):
    """ add setup kwargs from pev values, if not set in setup.cfg.

    :param pev:                 dict of project environment variables with a `'setup_kwargs'` dict to update/complete.

    optional setup_kwargs for native/implicit namespace packages are e.g. `namespace_packages`. adding to setup_kwargs
    `include_package_data=True` results in NOT including package resources into sdist (if no MANIFEST.in file is used).
    """
    kwargs: SetupKwargsType = pev['setup_kwargs']                                                       # type: ignore
    for arg_name, pev_key in (
            ('name', 'package_name'), ('version', 'package_version'), ('description', 'project_desc'),
            ('long_description_content_type', 'long_desc_type'), ('long_description', 'long_desc_content'),
            ('package_data', 'package_data'), ('packages', 'project_packages'),
            ('url', 'repo_url'), ('install_requires', 'install_require'), ('setup_requires', 'setup_require')):
        if arg_name not in kwargs and pev_key in pev:
            kwargs[arg_name] = pev[pev_key]

    if 'extras_require' not in kwargs:
        doc_req = cast(List[str], pev['docs_require'])
        tst_req = cast(List[str], pev['tests_require'])
        kwargs['extras_require'] = {'dev': cast(List[str], pev['dev_require']) + doc_req + tst_req,
                                    'docs': doc_req,
                                    'tests': tst_req, }

    if 'project_urls' not in kwargs:    # displayed on PyPI
        kwargs['project_urls'] = {'Documentation': pev['docs_url'],
                                  'Repository': pev['repo_url'],
                                  'Source': pev['docs_code'], }

    if 'zip_safe' not in kwargs:
        kwargs['zip_safe'] = not bool(cast(PackageDataType, pev['package_data'])[""])


def _init_app_configs(pev: PevType, cae: Any):
    pev_patch_section = pev_str(pev, 'PEV_DEFAULTS_SECTION_NAME')
    for name in cae.cfg_section_variable_names(pev_patch_section):
        pev[name] = cae.get_variable(name, section=pev_patch_section)


def _init_defaults(cae: Optional[Any], project_path: str) -> PevType:
    package_name = os.path.basename(project_path)
    setup_kwargs: SetupKwargsType = {}
    pev: PevType = {'package_name': package_name, 'project_path': project_path, 'setup_kwargs': setup_kwargs}

    for var_name, var_val in globals().items():
        if var_name.upper() == var_name:        # init imported ae.base and module constants like e.g. APP_PRJ
            pev[var_name] = var_val

    # add setuptools kwarg default values onto pev['setup_kwargs'] from (1) the setup.cfg or (2) STK-constants
    cfg_file_path = os.path.join(project_path, "setup.cfg")
    st_cfg = {}
    if os.path.isfile(cfg_file_path):   # suppress setuptools warning to remove setup.cfg if not exists
        try:
            st_cfg = read_configuration(cfg_file_path, ignore_option_errors=True)
        except DistutilsFileError:
            pass
    for var_name, var_val in pev.items():
        if var_name.startswith('STK_'):
            skn = var_name[4:].lower()
            var_val = st_cfg.get(skn, st_cfg.get('metadata', {}).get(skn, var_val))
            setup_kwargs[skn] = pev[var_name] = var_val     # not needed: globals()[var_name] = var_val
    setup_kwargs['name'] = st_cfg.get('metadata', {}).get('name', package_name)

    if cae:
        _init_app_configs(pev, cae)             # overwrite constants with cae app config vars
        _sync_stk_to_setup_kwargs(pev)

    return pev


def _init_pev(cae: Optional[Any], project_path: str) -> PevType:
    pev = _init_defaults(cae, project_path)

    package_name = pev_str(pev, 'package_name')                     # is also the repo project_name
    project_path = pev_str(pev, 'project_path')
    pev['pip_name'] = package_name.replace('_', '-')
    pev['namespace_name'] = namespace_name = namespace_guess(project_path)
    if namespace_name:
        pev['portion_name'] = portion_name = package_name[len(namespace_name) + 1:]
        pev['import_name'] = import_name = f"{namespace_name}.{portion_name}" if portion_name else namespace_name
    else:
        pev['portion_name'] = portion_name = ''
        pev['import_name'] = import_name = package_name
    pev['version_file'] = version_file = project_main_file(import_name, project_path=project_path)
    pev['package_version'] = code_file_version(version_file)        # is also the repo project_version

    pev['package_path'] = package_path = os.path.join(project_path, *namespace_name.split("."), portion_name)
    pev['package_data'] = find_package_data(package_path)

    root_prj, pkg_prj = pev_str(pev, 'ROOT_PRJ'), pev_str(pev, 'PACKAGE_PRJ')

    if os.path.isfile(os.path.join(project_path, pev_str(pev, 'BUILD_CONFIG_FILE'))):
        project_type = pev_str(pev, 'APP_PRJ')
    elif package_name == namespace_name + '_' + namespace_name:
        project_type = root_prj
    elif os.path.basename(version_file) == PY_INIT:
        project_type = pkg_prj
    elif os.path.basename(version_file) in (package_name + PY_EXT, portion_name + PY_EXT):
        project_type = pev_str(pev, 'MODULE_PRJ')
    elif os.path.basename(project_path) in pev_val(pev, 'PARENT_FOLDERS'):
        project_type = pev_str(pev, 'PARENT_PRJ')
    else:
        project_type = pev_str(pev, 'NO_PRJ')
    pev['project_type'] = project_type

    if namespace_name:
        find_packages_include = [namespace_name + (".*" if project_type in (pkg_prj, root_prj) else "")]
        pev['project_packages'] = setuptools.find_namespace_packages(where=project_path, include=find_packages_include)
        project_desc = f"{namespace_name} {project_type}" if project_type == root_prj else \
            f"{namespace_name} namespace {project_type} portion {portion_name}"
    else:
        pev['project_packages'] = setuptools.find_packages(where=project_path)
        project_desc = f"{package_name} {project_type}"
    pev['project_desc'] = f"{project_desc}: {code_file_title(version_file)}"

    return pev


def _load_descriptions(pev: PevType):
    """ load long description from the README file of the project.

    :param pev:                 dict of project environment variables with a `'project_path'` key.
    """
    path = pev_str(pev, 'project_path')
    file = os.path.join(path, 'README.rst')
    if os.path.isfile(file):
        pev['long_desc_type'] = 'text/x-rst'
        pev['long_desc_content'] = read_file(file)
    else:
        file = os.path.join(path, 'README.md')
        if os.path.isfile(file):
            pev['long_desc_type'] = 'text/markdown'
            pev['long_desc_content'] = read_file(file)


def _load_requirements(pev: PevType):
    """ load requirements from the available requirements.txt file(s) of this project.

    :param pev:                 dict of project environment variables with the following required project env vars:
                                DOCS_FOLDER, REQ_FILE_NAME, REQ_DEV_FILE_NAME, TESTS_FOLDER,
                                namespace_name, package_name, project_path.

                                the project env vars overwritten in this argument by this function are: dev_require,
                                docs_require, install_require, portions_packages, setup_require, tests_require.
    """
    def _package_list(req_file: str) -> List[str]:
        packages: List[str] = []
        if os.path.isfile(req_file):
            packages.extend(line.strip().split(' ')[0]                      # remove options, keep version number
                            for line in read_file(req_file).split('\n')
                            if line.strip()                                 # exclude empty lines
                            and not line.startswith('#')                    # exclude comments
                            and not line.startswith('-')                    # exclude -r/-e <req_file> lines
                            )
        return packages

    namespace_name = pev_str(pev, 'namespace_name')
    package_name = pev_str(pev, 'package_name')
    project_path = pev_str(pev, 'project_path')
    req_file_name = pev_str(pev, 'REQ_FILE_NAME')

    pev['dev_require'] = dev_require = _package_list(os.path.join(project_path, pev_str(pev, 'REQ_DEV_FILE_NAME')))

    prefix = f'{namespace_name}_'
    pev['portions_packages'] = [_ for _ in dev_require if _.startswith(prefix) and _ != prefix + namespace_name]

    pev['docs_require'] = _package_list(os.path.join(project_path, pev_str(pev, 'DOCS_FOLDER'), req_file_name))

    pev['install_require'] = _package_list(os.path.join(project_path, req_file_name))

    pev['setup_require'] = ['ae_base'] if package_name == 'aedev_setup_project' else ['aedev_setup_project']

    pev['tests_require'] = _package_list(os.path.join(project_path, pev_str(pev, 'TESTS_FOLDER'), req_file_name))


def _sync_stk_to_setup_kwargs(pev: PevType):
    setup_kwargs = cast(SetupKwargsType, pev['setup_kwargs'])
    for var_name, var_val in pev.items():
        if var_name.startswith('STK_'):
            setup_kwargs[var_name[4:].lower()] = var_val


# --------------- public helper functions --------------------------------------------------------------------------


def code_file_title(file_name: str) -> str:
    """ determine docstring title of a Python code file.

    :param file_name:           name (and optional path) of module/script file to read the docstring title number from.
    :return:                    docstring title string or empty string if file|docstring-title not found.
    """
    title = ""
    try:
        lines = read_file(file_name).split('\n')
        for idx, line in enumerate(lines):
            if line.startswith('"""'):
                title = (line[3:].strip() or lines[idx + 1].strip()).strip('"').strip()
                break
    except (FileNotFoundError, IndexError, OSError):
        pass
    return title


def code_file_version(file_name: str) -> str:
    """ read version of Python code file - from __version__ module variable initialization.

    :param file_name:           name (and optional path) of module/script file to read the version number from.
    :return:                    version number string or empty string if file or version-in-file not found.
    """
    try:
        content = read_file(file_name)
        version_match = re.search("^" + VERSION_PREFIX + "([^" + VERSION_QUOTE + "]*)" + VERSION_QUOTE, content, re.M)
    except (FileNotFoundError, OSError):
        version_match = None
    return version_match.group(1) if version_match else ""


def find_package_data(package_path: str) -> PackageDataType:
    """ find doc, template, kv, i18n translation text, image and sound files of an app or (namespace portion) package.

    :param package_path:        path of the directory tree root to collect: project root for app projects or the package
                                subdir (project_path/namespace_name/portion_name) for namespace projects.
    :return:                    setuptools package_data dict, where the key is an empty string (to be included for all
                                sub-packages) and the dict item is a list of all found resource files with a relative
                                path to the :paramref:`.package_path` directory. folder names with a leading underscore
                                (like e.g. the docs build, the `__pycache__` and `__enamlcache__` folders) get excluded.
                                explicitly included will be any :data:`~ae.base.BUILD_CONFIG_FILE` file, as well as any
                                file/folder names that are having a :data:`~ae.base.PACKAGE_INCLUDE_FILES_PREFIX`,
                                situated directly underneath the directory specified by :paramref:`.package_data`.
    """
    files = []

    def _add_file(file_name: str):
        if os.path.isfile(file_name):
            rel_path = os.path.relpath(file_name, package_path)
            if not any(_.startswith("_") for _ in rel_path.split(os.path.sep)):
                files.append(rel_path)

    _add_file(os.path.join(package_path, BUILD_CONFIG_FILE))

    for file in glob.glob(os.path.join(package_path, PACKAGE_INCLUDE_FILES_PREFIX + "*")):
        _add_file(file)     # add all files with PACKAGE_INCLUDE_FILES_PREFIX in package_path root folder
    for file in glob.glob(os.path.join(package_path, PACKAGE_INCLUDE_FILES_PREFIX + "*", "**", "*"), recursive=True):
        _add_file(file)     # add all file under package_path root folder names with the PACKAGE_INCLUDE_FILES_PREFIX

    docs_path = os.path.join(package_path, DOCS_FOLDER)
    for file in glob.glob(os.path.join(docs_path, "**", "*"), recursive=True):
        _add_file(file)

    tpl_path = os.path.join(package_path, TEMPLATES_FOLDER)
    for file in glob.glob(os.path.join(tpl_path, "**", "*"), recursive=True):
        _add_file(file)

    for file in glob.glob(os.path.join(package_path, "**", "*.kv"), recursive=True):
        _add_file(file)

    for resource_folder in ('img', 'loc', 'snd'):
        for file in glob.glob(os.path.join(package_path, resource_folder, "**", "*"), recursive=True):
            _add_file(file)

    return {"": files}


def namespace_guess(project_path: str) -> str:
    """ guess name of namespace name from the package/app/project root directory path.

    :param project_path:        path to project root folder.
    :return:                    namespace import name of the project specified via the project root directory path.
    """
    package_name = portion_name = os.path.basename(norm_path(project_path))
    join = os.path.join
    namespace_name = ""
    for part in package_name.split("_"):
        for path_parts in main_file_paths_parts(portion_name):
            if os.path.isfile(join(project_path, *path_parts)):
                return namespace_name[1:]

        project_path = os.path.join(project_path, part)
        *_ns_path_parts, portion_name = portion_name.split("_", maxsplit=1)
        namespace_name += "." + part

    return ""


def pev_str(pev: PevType, var_name: str) -> str:
    """ string value of project environment variable :paramref:`~pev_str.var_name` of :paramref:`~pev_str.pev`.

    :param pev:                 project environment variables dict.
    :param var_name:            name of variable.
    :return:                    variable value or if not exists in pev then the constant/default value of this module or
                                if there is no module constant with this name then an empty string.
    :raises AssertionError:     if the specified variable value is not of type `str`. in this case use the function
                                :func:`pev_val` instead.

    .. hint::
        the `str` type annotation of the return value makes mypy happy. additional the constant's values of this module
        will be taken into account. replaces `cast(str, pev.get('namespace_name', globals().get(var_name, "")))`.
    """
    val = pev_val(pev, var_name)
    assert isinstance(val, str), f"{var_name} value is not of type string (got {type(val)}). use pev_val() function!"
    return val


def pev_val(pev: PevType, var_name: str) -> PevVarType:
    """ determine value of project environment variable from passed pev or use module constant value as default.

    :param pev:                 project environment variables dict.
    :param var_name:            name of the variable to determine the value of.
    :return:                    project env var or module constant value. empty string if variable is not defined.
    """
    return pev.get(var_name, globals().get(var_name, ""))


def project_env_vars(project_path: str = "", cae: Optional[Any] = None, from_setup: bool = False) -> PevType:
    """ analyse and map the development environment of a package-/app-project into a dict of project property values.

    :param project_path:        optional rel/abs path of the package/app/project root directory of a new and existing
                                project (def=current working directory).
    :param cae:                 optional :class:`~ae.console.ConsoleApp` instance used to set/overwrite module constants
                                with the values from the app's :ref:`config variables <config-variables>`.
    :param from_setup:          pass True if this function get called from within the setup.py module of your project.
    :return:                    dict/mapping with the determined project environment variable values.
    """
    project_path = norm_path(project_path)
    setup_file = os.path.join(project_path, 'setup' + PY_EXT)

    if not from_setup and os.path.isfile(setup_file):
        with in_wd(project_path):
            # special import of project environment variables, to include package-specific patches/hook
            pev = getattr(import_module('setup'), 'pev', None)
            if isinstance(pev, dict):                                                       # PevType type
                if cae:
                    _init_app_configs(pev, cae)             # overwrite constants with cae app config vars
                    _sync_stk_to_setup_kwargs(pev)        # sync STK_* constants patched by app config to setup_kwargs
                return pev

    pev = _init_pev(cae, project_path)
    _load_requirements(pev)                         # load info from all *requirements.txt files
    _load_descriptions(pev)                         # load README* files
    _compile_remote_vars(pev)                       # compile the git host remote values
    _compile_setup_kwargs(pev)                      # compile 'setup_kwargs' variable value

    return pev
