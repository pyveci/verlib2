import sys

from verlib2 import __version__
from verlib2.distutils.version import LooseVersion, StrictVersion
from verlib2.packaging.version import Version


def test_version():
    if sys.version_info >= (3, 7):
        assert Version("0.0.0") <= Version(__version__)
    if sys.version_info >= (3, 8):
        assert LooseVersion("0.0.0") <= __version__
        assert StrictVersion("0.0.0") <= __version__
