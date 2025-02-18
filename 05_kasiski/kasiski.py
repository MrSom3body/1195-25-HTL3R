class Kasiski:
    def __init__(self, crypttext: str = "") -> None:
        self.crypttext = crypttext

    def allpos(self, text: str, substring: str) -> list[int]:
        """
        Calculates the positions of the substring in text.
        :param text: the text to look in
        :param substring: the substring to look for
        :return: a list with the indicies

        >>> k = Kasiski()
        >>> k.allpos("heissajuchei, ein ei", "ei")
        [1, 10, 14, 18]
        >>> k.allpos("heissajuchei, ein ei", "hai")
        []
        """
        return [
            i
            for i in range(len(text) - len(substring) + 1)
            if text[i : i + len(substring)] == substring
        ]

    def alldist(self, text: str, substring: str) -> set[int]:
        """
        Calculate all distances between all occurences of substring in text.
        :param text: the text to look in
        :param substring: the substring to look for
        :return: a list with the distances

        >>> k = Kasiski()
        >>> k.alldist("heissajuchei, ein ei", "ei")
        {4, 8, 9, 13, 17}
        >>> k.alldist("heissajuchei, ein ei", "hai")
        set()
        """
        dist: set[int] = set()
        pos = self.allpos(text, substring)
        for i in range(len(pos)):
            for j in range(i + 1, len(pos)):
                dist.add(pos[j] - pos[i])
        return dist


if __name__ == "__main__":
    import doctest

    _ = doctest.testmod()
