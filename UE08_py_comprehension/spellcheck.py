__author__ = "Karun Sandhu"

import string


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
            s.add(line.strip().lower())
    return s


def split_word(word: str) -> list[tuple[str, str]]:
    """
    Split a word into each possibility of two parts.
    :param word: the word to split:
    :return: list of tuple each containing one possibility of splitting the word.
    """
    return [(word[:i], word[i:]) for i in range(len(word) + 1)]


def edit1(word: str) -> set[str]:
    """
    Finds all words with an edit distance of 1.
    :param word: the word to find the variations for
    :return: set with all variations with an edit distance 1
    >>> edit1("abc")
    {'abjc', 'cbc', 'hbc', 'gabc', 'eabc', 'abm', 'abcm', 'iabc', 'tabc', 'akbc', 'abcx', 'aoc', 'aqbc', 'abac', 'abx', 'abpc', 'ablc', 'azbc', 'abec', 'abvc', 'awbc', 'ab', 'bc', 'abf', 'abh', 'mbc', 'abcg', 'arc', 'anc', 'vbc', 'abv', 'ajc', 'agbc', 'abyc', 'ayc', 'aec', 'gbc', 'abs', 'aac', 'qabc', 'abkc', 'bbc', 'aibc', 'vabc', 'abic', 'abn', 'abj', 'zbc', 'apc', 'uabc', 'abcd', 'labc', 'dbc', 'jabc', 'aybc', 'azc', 'sbc', 'ahbc', 'albc', 'awc', 'ajbc', 'obc', 'qbc', 'lbc', 'agc', 'aic', 'abi', 'abcl', 'abxc', 'rabc', 'abk', 'abqc', 'abq', 'abct', 'acb', 'abcp', 'abnc', 'xabc', 'abce', 'abl', 'abcr', 'abcu', 'tbc', 'kbc', 'axbc', 'aqc', 'abrc', 'axc', 'abz', 'atc', 'mabc', 'avbc', 'abc', 'fbc', 'akc', 'afc', 'aboc', 'kabc', 'abd', 'abu', 'ambc', 'abcv', 'abgc', 'abt', 'abcz', 'abca', 'rbc', 'abtc', 'habc', 'abcq', 'abhc', 'abcn', 'asc', 'abb', 'abe', 'acc', 'abci', 'aabc', 'jbc', 'nabc', 'abp', 'abr', 'abcf', 'babc', 'ybc', 'abwc', 'aobc', 'ubc', 'abmc', 'alc', 'abcs', 'wbc', 'acbc', 'arbc', 'yabc', 'aby', 'asbc', 'xbc', 'aubc', 'nbc', 'zabc', 'amc', 'absc', 'pabc', 'abbc', 'ahc', 'cabc', 'abcw', 'abuc', 'abzc', 'abcj', 'dabc', 'abw', 'anbc', 'ac', 'fabc', 'abck', 'abfc', 'aebc', 'pbc', 'ebc', 'ibc', 'abg', 'avc', 'bac', 'abch', 'oabc', 'apbc', 'aba', 'adc', 'abcb', 'wabc', 'abdc', 'abcy', 'abcc', 'auc', 'abco', 'sabc', 'atbc', 'afbc', 'abo', 'adbc'}
    >>> edit1("a")
    {'am', 'ka', 'z', 'r', 'ar', 'a', 'o', 'j', 'ua', 'aq', 'f', 'ao', 'p', 'ab', 'ad', 'y', 'va', 'm', 'ay', 'af', 'ah', 'ak', 'q', 'u', 'sa', 'ha', 'qa', 'pa', 'c', 'ea', 'ai', 'e', 'w', 'ag', 'l', 'au', 'wa', 'ga', 'xa', 'as', 'ra', 'ja', 'v', 'at', 'aw', 'aj', 'fa', 'x', 'da', 'g', 'k', 'ae', 'ac', 'ta', 'ca', 'ma', 'ba', 'd', 'na', 'n', 'b', 'ax', 'al', 'az', 'za', 'la', 'ia', 'av', 'aa', 'an', 'oa', 's', 'h', 'ya', 't', 'i', 'ap'}
    """
    sw = split_word(word)

    words = {w[0] + w[1][1:] for w in sw}
    words |= {
        w[0] + w[1][1:2] + w[1][0:1] + w[1][2:] for w in sw if len(w[1]) > 1
    }
    words |= {w[0] + ch + w[1][1:] for w in sw for ch in string.ascii_lowercase}
    words |= {w[0] + ch + w[1] for w in sw for ch in string.ascii_lowercase}
    words.discard("")
    return words


def edit1_good(word: str, dictionary: set[str]) -> set[str]:
    """
    Finds all possible corrections for a word.
    :param word: the mistyped word
    :return: set with possible completions
    """
    return edit1(word.lower()) & dictionary


def edit2_good(word: str, dictionary: set[str]) -> set[str]:
    """
    Does the same like edit2_good but with an edit distance of 2.
    :param word: the mistyped word
    :return: set with possible completions
    """
    return {w2 for w1 in edit1(word) for w2 in edit1(w1) if w2 in dictionary}


def correct(word: str, dictionary: list[str]) -> set[str]:
    """
    Finds the correction(s) for a given word.
    :param word: the word to correct
    :param dictionary: the list of valid words
    :return: set with corrections or empty set if nothing found

    >>> correct("hund", ["hund", "hand", "haus", "haut", "hans"])
    {'hund'}
    >>> correct("hudn", ["hund", "hand", "haus", "haut", "hans"])
    {'hund'}
    >>> correct("huns", ["hund", "hand", "haus", "haut", "hans"])
    {'haus', 'hund', 'hans'}
    >>> correct("xyz", ["hund", "hand", "haus", "haut", "hans"])
    set()
    """
    return (
        {word.lower()}
        if word.lower() in set(dictionary)
        else (
            edit1_good(word, set(dictionary))
            or edit2_good(word, set(dictionary))
            or set()
        )
    )


if __name__ == "__main__":
    import doctest

    _ = doctest.testmod()
