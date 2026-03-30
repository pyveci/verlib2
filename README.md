# verlib2

[![Tests](https://github.com/pyveci/verlib2/actions/workflows/main.yml/badge.svg)](https://github.com/pyveci/verlib2/actions/workflows/main.yml)
[![Test coverage](https://img.shields.io/codecov/c/gh/pyveci/verlib2.svg)](https://codecov.io/gh/pyveci/verlib2/)
[![Python versions](https://img.shields.io/pypi/pyversions/verlib2.svg)](https://pypi.org/project/verlib2/)

[![License](https://img.shields.io/github/license/pyveci/verlib2.svg)](https://github.com/pyveci/verlib2/blob/main/LICENSE)
[![Status](https://img.shields.io/pypi/status/verlib2.svg)](https://pypi.org/project/verlib2/)
[![PyPI](https://img.shields.io/pypi/v/verlib2.svg)](https://pypi.org/project/verlib2/)
[![Downloads](https://pepy.tech/badge/verlib2/month)](https://www.pepy.tech/projects/verlib2)


<!-- » [Documentation] -->

» [Changelog]
| [PyPI]
| [Issues]
| [Source code]
| [License]

[Changelog]: https://github.com/pyveci/verlib2/blob/main/CHANGES.md
[Documentation]: https://verlib2.readthedocs.io/
[Issues]: https://github.com/pyveci/verlib2/issues
[License]: https://github.com/pyveci/verlib2/blob/main/LICENSE
[PyPI]: https://pypi.org/project/verlib2/
[Source code]: https://github.com/pyveci/verlib2

## About

A standalone bundle of `distutils.version` and `packaging.version`,
without anything else.

[verlib] and [Distutils] are the implementations of [PEP 386].
[packaging.version] is the implementation of [PEP 440].
[verlib2] bundles both of them into a standalone package.

## Rationale

Everyone needs to compare versions, but no one wants to add `packaging` as a dependency.
`distutils` is deprecated, and Python 3.12 removed it from the standard library.

Following [PEP 632] to leave `distutils` behind, we found that people [started]
[bundling] [pep440.py] files into their projects, causing some redundancy across
the board.

## Setup

```shell
pip install verlib2
```

## Usage

```python
from verlib2 import Version

assert Version("1.0.dev456") < Version("1!1.2.rev33+123456") 
```

Note: The `verlib2.Version` symbol links to `verlib2.packaging.version`,
effectively providing packaging's `Version` class as the default variant.
Both implementations can be accessed like this:

```python
from verlib2.distutils.version import LooseVersion, StrictVersion
from verlib2.packaging.version import Version
```

## Acknowledgements

Alyssa Coghlan, Andrew Kuchling, Donald Stufft, Greg Stein, Greg Ward, Tarek Ziadé,
and all contributors to PEP-0386, PEP-0440 and their predecessors, including other
members of the Python Distutils-SIG and authors and contributors to the
[distutilsversion], [verlib], [distutils], [distutils2], [packaging.version]
packages.

## Other projects

Notable other projects are [pep440-rs] and [pep440-version-utils] if you need
better speed or more features. The former implements PEP440 in Rust, and the
latter makes it easier to handle version bumps, also following the PEP440
specification. Both packages require Python 3.8 and higher.

## Prior Art

We had a look at the [pep440], [pep440deb], [pep440nz], [pep440-utility], and
[version-utils], but apparently, they did not include what we have been looking for.

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

## Supported by

[![JetBrains logo.](https://resources.jetbrains.com/storage/products/company/brand/logos/jetbrains.svg)](https://jb.gg/OpenSourceSupport)

Special thanks to the people at JetBrains s.r.o. for supporting us with
excellent development tooling.


[bundling]: https://github.com/numpy/numpy/blob/v1.26.0/numpy/_utils/_pep440.py
[Distutils]: https://pypi.org/project/Distutils/
[distutils2]: https://hg.python.org/distutils2
[distutilsversion]: http://bitbucket.org/tarek/distutilsversion/
[packaging.version]: https://github.com/pypa/packaging/blob/main/src/packaging/version.py
[pep440]: https://pypi.org/project/pep440/
[pep440deb]: https://pypi.org/project/pep440deb/
[pep440nz]: https://pypi.org/project/pep440nz/
[pep440.py]: https://github.com/crate/crate-python/pull/513
[pep440-rs]: https://pypi.org/project/pep440-rs/
[pep440-utility]: https://pypi.org/project/pep440-utility/
[pep440-version-utils]: https://pypi.org/project/pep440-version-utils/
[PEP 386]: https://peps.python.org/pep-0386/
[PEP 440]: https://peps.python.org/pep-0440/
[PEP 632]: https://peps.python.org/pep-0632/
[started]: https://github.com/numpy/numpy/pull/21000
[verlib]: https://pypi.org/project/verlib/
[verlib2]: https://pypi.org/project/verlib2/
[version-utils]: https://pypi.org/project/version-utils/
