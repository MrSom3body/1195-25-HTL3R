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

    def encrypt(self, plaintext: str, key: str | None = None) -> str:
        """
        Encrypts a plaintext with the Caesar cipher.
        :param plaintext: the plaintext to be encrypted
        :param key: the key to be used for the encryption
        :return: the encrypted plaintext
        >>> caesar = Caesar()
        >>> caesar.encrypt("Hello, World!", "b")
        'ifmmpxpsme'
        >>> caesar.encrypt("Hello, World!", "f")
        'mjqqtbtwqi'
        """
        key = self.check_key(key, self.key)

        i_key = ord(key.lower()) - 97
        plaintext = self.to_lowercase_letter_only(plaintext)
        return "".join(
            [chr(((ord(ch) - 97 + i_key) % 26) + 97) for ch in plaintext]
        )

    def decrypt(self, crypttext: str, key: str | None = None) -> str:
        """
        Decrypts a ciphertext with the Caesar cipher.
        :param crypttext: the ciphertext to be decrypted
        :param key: the key to be used for the decryption
        :return: the decrypted ciphertext
        >>> caesar = Caesar()
        >>> caesar.decrypt("ifmmpxpsme", "b")
        'helloworld'
        >>> caesar.decrypt("mjqqtbtwqi", "f")
        'helloworld'
        """
        reverse_key = chr(
            (26 - (ord(self.check_key(key, self.key)) - 97)) % 26 + 97
        )
        return self.encrypt(crypttext, reverse_key)


if __name__ == "__main__":
    import doctest

    _ = doctest.testmod()
