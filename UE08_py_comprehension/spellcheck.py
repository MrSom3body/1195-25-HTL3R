__author__ = "Karun Sandhu"


def read_all_words(filename: str) -> set[str]:
    """
    Reads all words from a file into a set with all of the lowercase
    equivalents.
    :param filename: the file to read from
    :return: set with lowercased words
    """
    s: set[str] = set()
    with open(filename) as f:
        for line in f:
            s.add(line)
    return s


def split_word(word: str) -> list[tuple[str, str]]:
    """
    Split a word into each possibility of two parts.
    :param word: the word to split:
    :return: list of tuple each containing one possibility of splitting the word.
    """
    return [(word[:i], word[i:]) for i in range(len(word) + 1)]
