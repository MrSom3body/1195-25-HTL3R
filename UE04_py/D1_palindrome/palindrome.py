__author__ = "Karun Sandhu"


def is_palindrome(s: str) -> bool:
    """
    :param s: string to check if it is a palindrom
    :return: True if s is a palindrom, False otherwise
    """
    reverse = ""
    for ch in reversed(s):
        reverse += ch

    return s == reverse


def is_palindrome_sentence(s: str) -> bool:
    """
    :param s: string of a sentence to check if it is a palindrom
    :return: True if s is a palindrom, False otherwise
    """
    filtered = ""
    for ch in s:
        if ch.isalnum():
            filtered += ch

    return is_palindrome(filtered.lower())


def palindrome_product(x: int) -> int:
    """
    :param x: max value for the palindrome
    :return: a palindromic number (got by multiplying two 3-digit numbers) less than x
    """

    largest_palindrome = -1

    for a in range(999, 99, -1):
        for b in range(a, 99, -1):
            prod = a * b
            if prod >= x:
                continue
            elif prod < largest_palindrome:
                break
            if is_palindrome(str(prod)):
                largest_palindrome = prod

    return largest_palindrome


def to_base(number: int, base: int) -> str:
    """
    :param number: Zahl im 10er-System
    :param base: Zielsystem (maximal 36)
    :return: Zahl im Zielsystem als String
    >>> to_base(1234, 16)
    '4D2'
    """
    new_base = ""
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVXYZ"
    while number != 0:
        new_base = digits[number % base] + new_base
        number = number // base

    return new_base


def get_dec_hex_palindrome(x: int) -> int:
    """
    :param x: the number to look under for the highest decimal and hexadecimal palindrome
    :return: the highest number under x
    """
    for i in range(x, 0, -1):
        if is_palindrome(str(i)) and is_palindrome(str(to_base(i, 16))):
            return i
    return -1


if __name__ == "__main__":
    assert is_palindrome("anna")
    assert not is_palindrome("hello")
    assert is_palindrome("racecar")

    assert is_palindrome_sentence("Was it a car or a cat I saw?")
    assert not is_palindrome_sentence("This is not a palindrome.")
    assert is_palindrome_sentence("A man, a plan, a canal, Panama!")

    assert palindrome_product(1000000) == 906609  # 913 x 993
    assert palindrome_product(800000) == 793397  # 869 x 913
    assert palindrome_product(600000) == 595595  # 935 x 637

    import doctest

    _ = doctest.testmod()

    assert get_dec_hex_palindrome(1000) == 979
    assert get_dec_hex_palindrome(69420) == 41514
    assert get_dec_hex_palindrome(1_000_000) == 845548
