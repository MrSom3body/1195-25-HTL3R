__author__ = "Karun Sandhu"

import math


class Fraction:
    def __init__(self, numerator: int = 0, denominator: int = 1) -> None:
        if denominator == 0:
            raise ArithmeticError("Denominator can not be 0")

        gcd = math.gcd(numerator, denominator)
        self._numerator: int = int(numerator / gcd)
        self._denominator: int = int(denominator / gcd)
