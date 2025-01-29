class Caesar:
    def __init__(self, key: str | None = None) -> None:
        self.key: str = self.check_key(key)

    def check_key(self, key: str | None, fallback_key: str = "a") -> str:
        if key:
            if key.isalpha() and len(key) == 1:
                return key.lower()
            else:
                raise ValueError(f"The key must be a single letter, not: {key}")
        else:
            return self.check_key(fallback_key)

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
