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
