def unique(s):
    """
    Returns True only if the provided string consists of unique characters.
    """
    raise NotImplementedError


def test_unique():
    assert unique("house")
    assert not unique("direction")
