from __future__ import annotations


def is_module_from_legacy_bundled_package(module: str) -> bool:
    top_level = module.split(".", 1)[0]
    return top_level in legacy_bundled_packages


def approved_stub_package_exists(module: str) -> bool:
    top_level = module.split(".", 1)[0]
    if top_level in legacy_bundled_packages:
        return True
    if top_level in non_bundled_packages_flat:
        return True
    if top_level in non_bundled_packages_namespace:
        namespace = non_bundled_packages_namespace[top_level]
        components = module.split(".")
        for i in range(len(components), 0, -1):
            module = ".".join(components[:i])
            if module in namespace:
                return True
    return False


def stub_distribution_name(module: str) -> str | None:
    top_level = module.split(".", 1)[0]

    dist = legacy_bundled_packages.get(top_level)
    if dist:
        return dist
    dist = non_bundled_packages_flat.get(top_level)
    if dist:
        return dist

    if top_level in non_bundled_packages_namespace:
        namespace = non_bundled_packages_namespace[top_level]
        components = module.split(".")
        for i in range(len(components), 0, -1):
            module = ".".join(components[:i])
            dist = namespace.get(module)
            if dist:
                return dist

    return None


# Stubs for these third-party packages used to be shipped with mypy.
#
# Map package name to PyPI stub distribution name.
legacy_bundled_packages: dict[str, str] = {
    "aiofiles": "types-aiofiles",
    "bleach": "types-bleach",
    "boto": "types-boto",
    "cachetools": "types-cachetools",
    "click_spinner": "types-click-spinner",
    "contextvars": "types-contextvars",
    "croniter": "types-croniter",
    "dataclasses": "types-dataclasses",
    "dateparser": "types-dateparser",
    "dateutil": "types-python-dateutil",
    "decorator": "types-decorator",
    "deprecated": "types-Deprecated",
    "docutils": "types-docutils",
    "first": "types-first",
    "gflags": "types-python-gflags",
    "markdown": "types-Markdown",
    "mock": "types-mock",
    "OpenSSL": "types-pyOpenSSL",
    "paramiko": "types-paramiko",
    "pkg_resources": "types-setuptools",
    "polib": "types-polib",
    "pycurl": "types-pycurl",
    "pymysql": "types-PyMySQL",
    "pyrfc3339": "types-pyRFC3339",
    "python2": "types-six",
    "pytz": "types-pytz",
    "pyVmomi": "types-pyvmomi",
    "redis": "types-redis",
    "requests": "types-requests",
    "retry": "types-retry",
    "simplejson": "types-simplejson",
    "singledispatch": "types-singledispatch",
    "six": "types-six",
    "slugify": "types-python-slugify",
    "tabulate": "types-tabulate",
    "toml": "types-toml",
    "typed_ast": "types-typed-ast",
    "tzlocal": "types-tzlocal",
    "ujson": "types-ujson",
    "waitress": "types-waitress",
    "yaml": "types-PyYAML",
}

# Map package name to PyPI stub distribution name from typeshed.
# Stubs for these packages were never bundled with mypy. Don't
# include packages that have a release that includes PEP 561 type
# information.
#
# Note that these packages are omitted for now:
#   pika:       typeshed's stubs are on PyPI as types-pika-ts.
#               types-pika already exists on PyPI, and is more complete in many ways,
#               but is a non-typeshed stubs package.
non_bundled_packages_flat: dict[str, str] = {
    "MySQLdb": "types-mysqlclient",
    "PIL": "types-Pillow",
    "PyInstaller": "types-pyinstaller",
    "Xlib": "types-python-xlib",
    "aws_xray_sdk": "types-aws-xray-sdk",
    "babel": "types-babel",
    "braintree": "types-braintree",
    "bs4": "types-beautifulsoup4",
    "bugbear": "types-flake8-bugbear",
    "caldav": "types-caldav",
    "cffi": "types-cffi",
    "chevron": "types-chevron",
    "colorama": "types-colorama",
    "commonmark": "types-commonmark",
    "consolemenu": "types-console-menu",
    "crontab": "types-python-crontab",
    "d3dshot": "types-D3DShot",
    "dockerfile_parse": "types-dockerfile-parse",
    "docopt": "types-docopt",
    "editdistance": "types-editdistance",
    "entrypoints": "types-entrypoints",
    "farmhash": "types-pyfarmhash",
    "flake8_2020": "types-flake8-2020",
    "flake8_builtins": "types-flake8-builtins",
    "flake8_docstrings": "types-flake8-docstrings",
    "flake8_plugin_utils": "types-flake8-plugin-utils",
    "flake8_rst_docstrings": "types-flake8-rst-docstrings",
    "flake8_simplify": "types-flake8-simplify",
    "flake8_typing_imports": "types-flake8-typing-imports",
    "flask_cors": "types-Flask-Cors",
    "flask_migrate": "types-Flask-Migrate",
    "fpdf": "types-fpdf2",
    "gdb": "types-gdb",
    "hdbcli": "types-hdbcli",
    "html5lib": "types-html5lib",
    "httplib2": "types-httplib2",
    "humanfriendly": "types-humanfriendly",
    "invoke": "types-invoke",
    "jack": "types-JACK-Client",
    "jmespath": "types-jmespath",
    "jose": "types-python-jose",
    "jsonschema": "types-jsonschema",
    "keyboard": "types-keyboard",
    "ldap3": "types-ldap3",
    "nmap": "types-python-nmap",
    "oauthlib": "types-oauthlib",
    "openpyxl": "types-openpyxl",
    "opentracing": "types-opentracing",
    "parsimonious": "types-parsimonious",
    "passlib": "types-passlib",
    "passpy": "types-passpy",
    "peewee": "types-peewee",
    "pep8ext_naming": "types-pep8-naming",
    "playsound": "types-playsound",
    "psutil": "types-psutil",
    "psycopg2": "types-psycopg2",
    "pyaudio": "types-pyaudio",
    "pyautogui": "types-PyAutoGUI",
    "pycocotools": "types-pycocotools",
    "pyflakes": "types-pyflakes",
    "pygments": "types-Pygments",
    "pyi_splash": "types-pyinstaller",
    "pynput": "types-pynput",
    "pythoncom": "types-pywin32",
    "pythonwin": "types-pywin32",
    "pyscreeze": "types-PyScreeze",
    "pysftp": "types-pysftp",
    "pytest_lazyfixture": "types-pytest-lazy-fixture",
    "pywintypes": "types-pywin32",
    "regex": "types-regex",
    "send2trash": "types-Send2Trash",
    "slumber": "types-slumber",
    "stdlib_list": "types-stdlib-list",
    "stripe": "types-stripe",
    "toposort": "types-toposort",
    "tqdm": "types-tqdm",
    "tree_sitter": "types-tree-sitter",
    "tree_sitter_languages": "types-tree-sitter-languages",
    "ttkthemes": "types-ttkthemes",
    "vobject": "types-vobject",
    "whatthepatch": "types-whatthepatch",
    "win32": "types-pywin32",
    "win32api": "types-pywin32",
    "win32con": "types-pywin32",
    "win32com": "types-pywin32",
    "win32comext": "types-pywin32",
    "win32gui": "types-pywin32",
    "xmltodict": "types-xmltodict",
    "zxcvbn": "types-zxcvbn",
    # Stub packages that are not from typeshed
    # Since these can be installed automatically via --install-types, we have a high trust bar
    # for additions here
    "pandas": "pandas-stubs",  # https://github.com/pandas-dev/pandas-stubs
    "lxml": "lxml-stubs",  # https://github.com/lxml/lxml-stubs
}


non_bundled_packages_namespace: dict[str, dict[str, str]] = {
    "backports": {"backports.ssl_match_hostname": "types-backports.ssl_match_hostname"},
    "google": {"google.cloud.ndb": "types-google-cloud-ndb", "google.protobuf": "types-protobuf"},
    "paho": {"paho.mqtt": "types-paho-mqtt"},
}
