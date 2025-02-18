import string


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

    def crack(self, crypttext: str, elements: int = 1) -> list[str] | None:
        """
        Gets the most likely keys for a given ciphertext in German.
        :param crypttext: the ciphertext to crack
        :param elements: the number of possible keys to return
        :return: a list of the most likely keys

        >>> str = 'Vor einem großen Walde wohnte ein armer Holzhacker mit seiner Frau und seinen zwei Kindern; das Bübchen hieß Hänsel und das Mädchen Gretel. Er hatte wenig zu beißen und zu brechen, und einmal, als große Teuerung ins Land kam, konnte er das tägliche Brot nicht mehr schaffen. Wie er sich nun abends im Bette Gedanken machte und sich vor Sorgen herumwälzte, seufzte er und sprach zu seiner Frau: "Was soll aus uns werden? Wie können wir unsere armen Kinder ernähren da wir für uns selbst nichts mehr haben?"'
        >>> caesar = Caesar()
        >>> caesar.crack(str)
        ['a']
        >>> caesar.crack(str, 100) # can't be more than 26
        ['a', 'n', 'j', 'w', 'e', 'r', 'z', 'k', 'b', 'o', 'm', 'l', 'q', 'v', 'p', 'f', 'u', 'h', 'd', 't', 's', 'y', 'i', 'g', 'x', 'c']
        >>> crypted = caesar.encrypt(str, "y")
        >>> caesar.crack(crypted, 3)
        ['y', 'l', 'h']
        """

        sanitized_crypttext: str = self.to_lowercase_letter_only(crypttext)
        length: int = len(sanitized_crypttext)
        letter_frequency: dict[str, float] = {}
        german_letter_frequency: dict[str, float] = {
            "a": 0.0651,
            "b": 0.0189,
            "c": 0.0306,
            "d": 0.0508,
            "e": 0.1740,
            "f": 0.0166,
            "g": 0.0301,
            "h": 0.0476,
            "i": 0.0755,
            "j": 0.0027,
            "k": 0.0121,
            "l": 0.0344,
            "m": 0.0253,
            "n": 0.0978,
            "o": 0.0251,
            "p": 0.0079,
            "q": 0.0002,
            "r": 0.0700,
            "s": 0.0727,
            "t": 0.0615,
            "u": 0.0435,
            "v": 0.0067,
            "w": 0.0189,
            "x": 0.0003,
            "y": 0.0004,
            "z": 0.0113,
        }

        for letter in string.ascii_lowercase:
            letter_frequency[letter] = (
                sanitized_crypttext.count(letter) / length
            )

        possible_keys_dict: dict[str, float] = {}
        for current_shift in range(26):
            distance = 0
            for letter in german_letter_frequency:
                shifted_letter = chr(
                    ord("a") + (ord(letter) - ord("a") + current_shift) % 26
                )
                observed_frequency = letter_frequency.get(shifted_letter, 0)
                expected_frequency = german_letter_frequency[letter]
                distance += (observed_frequency - expected_frequency) ** 2

            possible_keys_dict[chr(ord("a") + current_shift)] = distance

        return [
            kv[0]
            for kv in sorted(
                possible_keys_dict.items(), key=lambda item: item[1]
            )
        ][:elements]


if __name__ == "__main__":
    import doctest

    _ = doctest.testmod()
