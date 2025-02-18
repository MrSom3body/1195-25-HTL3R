from .caesar import Caesar


class Vigenere:
    def __init__(self, key: str | None = None) -> None:
        self.key: str = self.check_key(key)
        self.caesar: Caesar = Caesar()

    def check_key(self, key: str | None, fallback_key: str = "a") -> str:
        if key:
            if key.isalpha():
                return key.lower()
            else:
                raise ValueError(f"The key must only contain letters: {key}")
        else:
            return self.check_key(fallback_key)


if __name__ == "__main__":
    import doctest

    _ = doctest.testmod()
