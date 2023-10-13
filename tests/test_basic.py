from verlib2 import Version


def test_version():
    assert (
        Version("1.0.dev456")
        < Version("1.0a2.dev456")
        < Version("1!1.0b1.dev456")
        < Version("1!1.2.rev33+123456")
    )
