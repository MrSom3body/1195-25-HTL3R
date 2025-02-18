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

    def encrypt(self, plaintext: str, key: str | None = None) -> str:
        """
        Encrypts a plaintext with the Vigenere cipher.
        :param plaintext: the plaintext to be encrypted
        :param key: the key to be used for the encryption
        :return: the encrypted plaintext

        >>> vigenere = Vigenere()
        >>> vigenere.encrypt("hello", "abcde")
        'hfnos'

        >>> vigenere.encrypt("attackatdawn", "lemon")
        'lxfopvefrnhr'

        >>> vigenere.encrypt("", "abcd")
        ''
        >>> vigenere.encrypt("hello", "ABCDE d 1 213 12")
        Traceback (most recent call last):
        ...
        ValueError: The key must only contain letters: ABCDE d 1 213 12
        """
        key = self.check_key(key, self.key)
        encrypted = ""

        for index, ch in enumerate(plaintext):
            encrypted += self.caesar.encrypt(ch, key[index % len(key)])

        return encrypted


if __name__ == "__main__":
    import doctest

    _ = doctest.testmod()
