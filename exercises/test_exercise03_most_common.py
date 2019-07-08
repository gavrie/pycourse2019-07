def most_common_word(text):
    """
    Returns the most commonly occurring word in the provided string.
    """
    raise NotImplementedError


def test_most_common_word():
    assert most_common_word("the quick brown fox jumps over the lazy dog") == "the"
    assert most_common_word("to be or not to be that is the question to ask") == "to"
