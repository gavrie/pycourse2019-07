def wordcount(text):
    """
    Returns the number of words in the provided string.
    """
    raise NotImplementedError


def test_wordcount():
    assert wordcount("hello world") == 2
    assert wordcount("the hitchhiker's guide to the galaxy") == 6
