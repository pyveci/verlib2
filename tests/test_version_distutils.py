"""Tests for distutils.version."""

import pytest

import verlib2
from verlib2.distutils.version import LooseVersion, StrictVersion


@pytest.fixture(autouse=True)
def suppress_deprecation():
    with verlib2.distutils.version.suppress_known_deprecation():
        yield


class TestVersion:
    def test_prerelease(self):
        version = StrictVersion("1.2.3a1")
        assert version.version == (1, 2, 3)
        assert version.prerelease == ("a", 1)
        assert str(version) == "1.2.3a1"

        version = StrictVersion("1.2.0")
        assert str(version) == "1.2"

    def test_cmp_strict(self):
        versions = (
            ("1.5.1", "1.5.2b2", -1),
            ("161", "3.10a", ValueError),
            ("8.02", "8.02", 0),
            ("3.4j", "1996.07.12", ValueError),
            ("3.2.pl0", "3.1.1.6", ValueError),
            ("2g6", "11g", ValueError),
            ("0.9", "2.2", -1),
            ("1.2.1", "1.2", 1),
            ("1.1", "1.2.2", -1),
            ("1.2", "1.1", 1),
            ("1.2.1", "1.2.2", -1),
            ("1.2.2", "1.2", 1),
            ("1.2", "1.2.2", -1),
            ("0.4.0", "0.4", 0),
            ("1.13++", "5.5.kw", ValueError),
        )

        for v1, v2, wanted in versions:
            try:
                res = StrictVersion(v1)._cmp(StrictVersion(v2))
            except ValueError as ex:
                if wanted is ValueError:
                    continue
                raise AssertionError(
                    f"cmp({v1}, {v2}) shouldn't raise ValueError"
                ) from ex
            assert res == wanted, f"cmp({v1}, {v2}) should be {wanted}, got {res}"
            res = StrictVersion(v1)._cmp(v2)
            assert res == wanted, f"cmp({v1}, {v2}) should be {wanted}, got {res}"
            res = StrictVersion(v1)._cmp(object())
            assert res is NotImplemented, (
                f"cmp({v1}, {v2}) should be NotImplemented, got {res}"
            )

    def test_cmp_loose(self):
        versions = (
            ("1.5.1", "1.5.2b2", -1),
            ("161", "3.10a", 1),
            ("8.02", "8.02", 0),
            ("3.4j", "1996.07.12", -1),
            ("3.2.pl0", "3.1.1.6", 1),
            ("2g6", "11g", -1),
            ("0.960923", "2.2beta29", -1),
            ("1.13++", "5.5.kw", -1),
        )

        for v1, v2, wanted in versions:
            res = LooseVersion(v1)._cmp(LooseVersion(v2))
            assert res == wanted, f"cmp({v1}, {v2}) should be {wanted}, got {res}"
            res = LooseVersion(v1)._cmp(v2)
            assert res == wanted, f"cmp({v1}, {v2}) should be {wanted}, got {res}"
            res = LooseVersion(v1)._cmp(object())
            assert res is NotImplemented, (
                f"cmp({v1}, {v2}) should be NotImplemented, got {res}"
            )

    def test_cmp_more(self):
        assert LooseVersion("1.5.1") < LooseVersion("1.5.2b2")
        assert LooseVersion("1.5.1") <= LooseVersion("1.5.2b2")
        assert LooseVersion("1.5.1") == LooseVersion("1.5.1")
        assert LooseVersion("1.5.2") > LooseVersion("1.5.1")
        assert LooseVersion("1.5.2") >= LooseVersion("1.5.1")
        assert StrictVersion("1.2.3a1") < StrictVersion("1.2.3b2")
        assert StrictVersion("1.2.3a1") < StrictVersion("1.2.3")
        assert StrictVersion("1.2.3") > StrictVersion("1.2.3a1")
        assert StrictVersion("1.2.3b2") > StrictVersion("1.2.3a1")
        assert repr(StrictVersion("1.2.3a1")) == "StrictVersion ('1.2.3a1')"
        assert repr(LooseVersion("1.2.3")) == "LooseVersion ('1.2.3')"
