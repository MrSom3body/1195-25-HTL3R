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
    {'abjc', 'hbc', 'gabc', 'iabc', 'tabc', 'akbc', 'abcx', 'aoc', 'aqbc', 'abac', 'abpc', 'azbc', 'abec', 'awbc', 'ab', 'mbc', 'arc', 'anc', 'vbc', 'agbc', 'aec', 'gbc', 'abs', 'aac', 'qabc', 'aibc', 'vabc', 'abic', 'abn', 'abj', 'zbc', 'apc', 'labc', 'dbc', 'jabc', 'aybc', 'azc', 'ahbc', 'albc', 'ajbc', 'aic', 'lbc', 'abi', 'abcl', 'rabc', 'abqc', 'abq', 'abnc', 'abl', 'axbc', 'abrc', 'mabc', 'avbc', 'abc', 'akc', 'ambc', 'abgc', 'abt', 'abcz', 'rbc', 'abtc', 'habc', 'abcq', 'abhc', 'abcn', 'asc', 'abb', 'abe', 'aabc', 'jbc', 'abp', 'abr', 'abcf', 'abwc', 'abmc', 'arbc', 'asbc', 'xbc', 'aubc', 'nbc', 'zabc', 'pabc', 'ahc', 'cabc', 'abcw', 'abcj', 'dabc', 'fabc', 'abck', 'aebc', 'abch', 'adc', 'wabc', 'abdc', 'abcc', 'auc', 'atbc', 'abo', 'cbc', 'eabc', 'abm', 'abcm', 'abx', 'ablc', 'abvc', 'bc', 'abf', 'abh', 'abcg', 'abv', 'ajc', 'abyc', 'ayc', 'abkc', 'bbc', 'uabc', 'abcd', 'sbc', 'awc', 'obc', 'qbc', 'agc', 'abxc', 'abk', 'abct', 'acb', 'xabc', 'abcp', 'abce', 'abcr', 'abcu', 'tbc', 'kbc', 'aqc', 'axc', 'abz', 'atc', 'fbc', 'afc', 'aboc', 'kabc', 'abd', 'abu', 'abcv', 'abca', 'acc', 'abci', 'nabc', 'babc', 'ybc', 'aobc', 'ubc', 'alc', 'abcs', 'wbc', 'acbc', 'yabc', 'aby', 'amc', 'absc', 'abbc', 'abuc', 'abzc', 'abw', 'anbc', 'ac', 'abfc', 'pbc', 'ebc', 'ibc', 'abg', 'avc', 'bac', 'oabc', 'apbc', 'aba', 'abcb', 'abcy', 'abco', 'sabc', 'afbc', 'adbc'}
    >>> edit1("a")
    {'am', 'ka', 'a', 'o', 'ua', 'aq', 'f', 'ao', 'p', 'ab', 'va', 'ay', 'af', 'sa', 'qa', 'c', 'ai', 'e', 'ga', 'ra', 'ja', 'at', 'aw', 'aj', 'g', 'k', 'ae', 'ta', 'ca', 'd', 'b', 'ia', 'av', 's', 'h', 'ya', 'i', 'z', 'r', 'ar', 'j', 'ad', 'y', 'm', 'ah', 'ak', 'q', 'u', 'ha', 'pa', 'ea', 'wa', 'ag', 'w', 'l', 'au', 'xa', 'as', 'v', 'fa', 'x', 'da', 'ac', 'ma', 'ba', 'na', 'n', 'ax', 'za', 'al', 'az', 'la', 'aa', 'an', 'oa', 't', 'ap'}
    """
    sw = split_word(word)

    words = (
        {w[0] + w[1][1:] for w in sw}.union(
            w[0] + w[1][1:2] + w[1][0:1] + w[1][2:] for w in sw if len(w[1]) > 1
        )
        .union(
            w[0] + ch + w[1][1:] for w in sw for ch in string.ascii_lowercase
        )
        .union(w[0] + ch + w[1] for w in sw for ch in string.ascii_lowercase)
    )
    words.discard("")
    return words


if __name__ == "__main__":
    import doctest

    _ = doctest.testmod()
