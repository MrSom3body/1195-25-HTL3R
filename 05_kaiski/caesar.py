class Caesar:
    def __init__(self, key: str = "") -> None:
        self.key: str = key

    def to_lowercase_letter_only(self, plaintext: str) -> str:
        """
        Changes the plaintext to lowercase and removes all non-letter characters.
        :param plaintext: the plaintext to be changed to lowercase and letters only
        :return: the plaintext in lowercase and letters only
        >>> caesar = Caesar()
        >>> caesar.to_lowercase_letter_only("Hello, World!")
        'helloworld'
        >>> caesar.to_lowercase_letter_only("Hello,#+14123     World!")
        'helloworld'
        """
        return "".join([ch.lower() for ch in plaintext if ch.isalpha()])


if __name__ == "__main__":
    import doctest

    _ = doctest.testmod()
