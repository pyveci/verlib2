# verlib2

[![Tests](https://github.com/panodata/verlib2/actions/workflows/main.yml/badge.svg)](https://github.com/panodata/verlib2/actions/workflows/main.yml)
[![Test coverage](https://img.shields.io/codecov/c/gh/panodata/verlib2.svg)](https://codecov.io/gh/panodata/verlib2/)
[![Python versions](https://img.shields.io/pypi/pyversions/verlib2.svg)](https://pypi.org/project/verlib2/)

[![License](https://img.shields.io/github/license/panodata/verlib2.svg)](https://github.com/panodata/verlib2/blob/main/LICENSE)
[![Status](https://img.shields.io/pypi/status/verlib2.svg)](https://pypi.org/project/verlib2/)
[![PyPI](https://img.shields.io/pypi/v/verlib2.svg)](https://pypi.org/project/verlib2/)
[![Downloads](https://pepy.tech/badge/verlib2/month)](https://www.pepy.tech/projects/verlib2)


<!-- » [Documentation] -->

» [Changelog]
| [PyPI]
| [Issues]
| [Source code]
| [License]

[Changelog]: https://github.com/panodata/verlib2/blob/main/CHANGES.md
[Documentation]: https://verlib2.readthedocs.io/
[Issues]: https://github.com/panodata/verlib2/issues
[License]: https://github.com/panodata/verlib2/blob/main/LICENSE
[PyPI]: https://pypi.org/project/verlib2/
[Source code]: https://github.com/panodata/verlib2


## About

A standalone variant of `packaging.version`, without anything else.

[verlib] is the implementation of [PEP 386]. [verlib2] is the implementation of [PEP 440]. 


## Rationale

Everyone needs to compare versions, but no one wants to add `packaging` as a dependency.
`distutils` is deprecated, and Python 3.12 removed it from the standard library.


## Setup

```shell
pip install verlib2
```


## Usage
```
from verlib2 import Version

assert Version("1.0.dev456") < Version("1!1.2.rev33+123456") 
```


## Acknowledgements

Tarek Ziadé, Donald Stufft, and all contributors to `distutilsversion`, `verlib`,
`distutils`, `distutils2`, `packaging.version`, PEP-0386, PEP-0440, and most
probably more.


## Prior Art

- https://peps.python.org/pep-0386/
- https://peps.python.org/pep-0440/
- http://bitbucket.org/tarek/distutilsversion/
- https://pypi.org/project/verlib/
- https://hg.python.org/distutils2
- https://github.com/pypa/packaging/blob/23.2/src/packaging/version.py
- https://github.com/numpy/numpy/pull/21000
- https://github.com/numpy/numpy/blob/v1.26.0/numpy/_utils/_pep440.py
- https://github.com/crate/crate-python/pull/513
- https://pypi.org/search/?q=pep440
- https://pypi.org/project/pep440/
- https://pypi.org/project/pep440deb/
- https://pypi.org/project/pep440nz/
- https://pypi.org/project/pep440-rs/
- https://pypi.org/project/pep440-utility/
- https://pypi.org/project/pep440-version-utils/
- https://pypi.org/project/version-utils/


## Development

Set up package in development mode.
```shell
python3 -m venv .venv
source .venv/bin/activate
pip install --editable='.[develop,test]'
```

Run software tests.
```shell
poe check
```



[verlib]: https://pypi.org/project/verlib/
[verlib2]: https://pypi.org/project/verlib2/
[PEP 386]: https://peps.python.org/pep-0386/
[PEP 440]: https://peps.python.org/pep-0440/
