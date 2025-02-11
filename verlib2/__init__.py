# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.

__title__ = "verlib2"
__summary__ = (
    "A standalone variant of distutils.version "
    "and packaging.version, without anything else"
)
__uri__ = "https://github.com/pyveci/verlib2"
__author__ = "Greg Ward, Donald Stufft, and individual contributors"

__license__ = "BSD-2-Clause or Apache-2.0"
__copyright__ = "2014 %s" % __author__

try:
    from importlib.metadata import PackageNotFoundError, version
except (ImportError, ModuleNotFoundError):  # pragma:nocover
    from importlib_metadata import (  # type: ignore[assignment,no-redef,unused-ignore]
        PackageNotFoundError,
        version,
    )

__appname__ = "verlib2"

try:
    __version__ = version(__appname__)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"

from verlib2.packaging.version import Version  # noqa: F401
