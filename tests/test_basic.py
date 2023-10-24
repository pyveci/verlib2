from verlib2 import Version


def test_version():
    assert (
        Version("1.0.dev456")
        < Version("1.0a2.dev456")
        < Version("1!1.0b1.dev456")
        < Version("1!1.2.rev33+123456")
    )


def test_distutils_backward_compatibility():
    """
    The `LooseVersion` and `StrictVersion` classes of `distutils.version`
    had a `version` property, mirroring the `release` property of
    `packaging.version`.

    This test verifies it is in place.
    """
    version = Version("1.0.dev456")
    assert version.version == (1, 0)
