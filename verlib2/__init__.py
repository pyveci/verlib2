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

__version__ = "0.1.0"

__license__ = "BSD-2-Clause or Apache-2.0"
__copyright__ = "2014 %s" % __author__


from verlib2.packaging.version import Version  # noqa: F401
