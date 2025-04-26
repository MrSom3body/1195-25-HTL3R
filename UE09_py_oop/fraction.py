__author__ = "Karun Sandhu"

import math
from typing import override


class Fraction:
    def __init__(self, numerator: int = 0, denominator: int = 1) -> None:
        if denominator == 0:
            raise ArithmeticError("Denominator can not be 0")

        gcd = math.gcd(numerator, denominator)
        self._numerator: int = int(numerator / gcd)
        self._denominator: int = int(denominator / gcd)

    @override
    def __str__(self) -> str:
        if self._numerator > self._denominator:
            full = self._numerator // self._denominator
            remainder = self._numerator % self._denominator
            if remainder == 0:
                return str(full)
            else:
                return f"{full} {remainder}/{self._denominator}"
        else:
            return f"{self._numerator}/{self._denominator}"
