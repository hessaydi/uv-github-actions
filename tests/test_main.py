from yt_uv import add, multiply, hello


def test_hello():
    assert hello() == "Hello from yt-uv!"


def test_add():
    assert add(1, 2) == 3


def test_multiply():
    assert multiply(2.5, 2) == 5
