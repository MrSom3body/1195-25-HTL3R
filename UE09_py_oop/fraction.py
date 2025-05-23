__author__ = "Karun Sandhu"

import math
from types import NotImplementedType
from typing import override


class Fraction:
    def __init__(self, numerator: int = 0, denominator: int = 1) -> None:
        """
        Initialize a new Fraction.

        :param numerator: numerator (default 0)
        :param denominator: denominator (default 1)
        :raises ArithmeticError: if denominator is zero

        >>> Fraction(3, -6)
        Fraction(-1, 2)
        >>> Fraction(4, 2)
        Fraction(2, 1)
        """
        if denominator == 0:
            raise ArithmeticError("Denominator can not be 0")

        if denominator < 0:
            numerator = -numerator
            denominator = -denominator

        gcd = math.gcd(numerator, denominator)
        self._numerator: int = int(numerator / gcd)
        self._denominator: int = int(denominator / gcd)

    @property
    def numerator(self) -> int:
        """
        Get numerator.

        :return: int

        >>> Fraction(3, 4).numerator
        3
        """
        return self._numerator

    @property
    def denominator(self) -> int:
        """
        Get denominator.

        :return: int

        >>> Fraction(3, 4).denominator
        4
        """
        return self._denominator

    @override
    def __str__(self) -> str:
        """
        String representation for print().

        :return: str

        >>> str(Fraction(3, 2))
        '1 1/2'
        >>> str(Fraction(1, 4))
        '1/4'
        """
        if self._numerator > self._denominator:
            full = self._numerator // self._denominator
            remainder = self._numerator % self._denominator
            if remainder == 0:
                return str(full)
            else:
                return f"{full} {remainder}/{self._denominator}"
        else:
            return f"{self._numerator}/{self._denominator}"

    @override
    def __repr__(self) -> str:
        """
        Official representation.

        :return: str

        >>> repr(Fraction(1, 2))
        'Fraction(1, 2)'
        """
        return f"Fraction({self._numerator}, {self._denominator})"

    def __float__(self) -> float:
        """
        Convert to float.

        :return: float

        >>> float(Fraction(1, 2))
        0.5
        """
        return self._numerator / self._denominator

    @override
    def __eq__(self, otherfraction: object) -> bool | NotImplementedType:
        """
        Check equality.

        :param other: Fraction or int
        :return: bool

        >>> Fraction(1, 2) == Fraction(2, 4)
        True
        >>> Fraction(1, 2) == 0.5
        True
        >>> Fraction(1, 2) == 0.6
        False
        """
        if isinstance(otherfraction, Fraction):
            return (
                self._numerator == otherfraction._numerator
                and self._denominator == otherfraction._denominator
            )
        elif isinstance(otherfraction, int):
            return self._numerator == otherfraction * self._denominator
        elif isinstance(otherfraction, float):
            return float(self) == otherfraction
        else:
            return NotImplemented

    def __lt__(self, otherfraction: object) -> bool | NotImplementedType:
        """
        Check less-than.

        :param other: Fraction, int or float
        :return: bool

        >>> Fraction(1, 2) < Fraction(3, 4)
        True
        >>> Fraction(1, 2) < 1
        True
        >>> Fraction(1, 2) < 0.6
        True
        >>> Fraction(1, 2) < 0.4
        False
        """
        if isinstance(otherfraction, Fraction):
            return (
                self._numerator * otherfraction._denominator
                < otherfraction._numerator * self._denominator
            )
        elif isinstance(otherfraction, int):
            return self._numerator < otherfraction * self._denominator
        elif isinstance(otherfraction, float):
            return float(self) < otherfraction
        else:
            return NotImplemented

    def __add__(self, otherfraction: "Fraction | int") -> "Fraction":
        """
        Add fractions or int.

        :param otherfraction: Fraction or int
        :return: Fraction

        >>> Fraction(1, 2) + Fraction(1, 4)
        Fraction(3, 4)
        >>> Fraction(1, 2) + 1
        Fraction(3, 2)
        """
        if isinstance(otherfraction, Fraction):
            return Fraction(
                self._numerator * otherfraction._denominator
                + self._denominator * otherfraction._numerator,
                self._denominator * otherfraction._denominator,
            )
        else:
            return Fraction(
                self._numerator + otherfraction * self._denominator,
                self._denominator,
            )

    def __radd__(self, otherfraction: "Fraction | int") -> "Fraction":
        """
        Reverse addition.

        :param otherfraction: int or Fraction
        :return: Fraction

        >>> 1 + Fraction(1, 2)
        Fraction(3, 2)
        """
        return self.__add__(otherfraction)

    def __sub__(self, otherfraction: "Fraction | int") -> "Fraction":
        """
        Subtract fractions or int.

        :param otherfraction: Fraction or int
        :return: Fraction

        >>> Fraction(1, 2) - Fraction(1, 4)
        Fraction(1, 4)
        >>> Fraction(1, 2) - 1
        Fraction(-1, 2)
        """
        if isinstance(otherfraction, Fraction):
            return Fraction(
                self._numerator * otherfraction._denominator
                - self._denominator * otherfraction._numerator,
                self._denominator * otherfraction._denominator,
            )
        else:
            return Fraction(
                self._numerator - otherfraction * self._denominator,
                self._denominator,
            )

    def __rsub__(self, otherfraction: "Fraction | int") -> "Fraction":
        """
        Reverse subtraction.

        :param other: int or Fraction
        :return: Fraction

        >>> 1 - Fraction(1, 2)
        Fraction(1, 2)
        """
        if isinstance(otherfraction, Fraction):
            return Fraction(
                otherfraction._numerator * self._denominator
                - self._numerator * otherfraction._denominator,
                otherfraction._denominator * self._denominator,
            )
        else:
            return Fraction(
                otherfraction * self._denominator - self._numerator,
                self._denominator,
            )

    def __mul__(self, otherfraction: "Fraction | int"):
        """
        Multiply fractions or int.

        :param other: Fraction or int
        :return: Fraction

        >>> Fraction(1, 2) * Fraction(2, 3)
        Fraction(1, 3)
        >>> Fraction(1, 2) * 2
        Fraction(1, 1)
        """
        if isinstance(otherfraction, Fraction):
            return Fraction(
                self._numerator * otherfraction._numerator,
                self._denominator * otherfraction._denominator,
            )
        else:
            return Fraction(self._numerator * otherfraction, self._denominator)

    def __rmul__(self, otherfraction: "Fraction | int"):
        """
        Reverse multiplication.

        :param otherfraction: int or Fraction
        :return: Fraction

        >>> 2 * Fraction(1, 2)
        Fraction(1, 1)
        """
        return self.__mul__(otherfraction)

    def __truediv__(self, otherfraction: "Fraction | int") -> "Fraction":
        """
        Divide by fraction or int.

        :param othefractionrfraction: Fraction or int
        :raises ZeroDivisionError: if dividing by zero
        :return: Fraction

        >>> Fraction(1, 2) / Fraction(1, 4)
        Fraction(2, 1)
        >>> Fraction(1, 2) / 2
        Fraction(1, 4)
        """
        if isinstance(otherfraction, Fraction):
            if otherfraction._numerator == 0:
                raise ZeroDivisionError("Division by zero fraction")
            return Fraction(
                self._numerator * otherfraction._denominator,
                self._denominator * otherfraction._numerator,
            )
        else:
            if otherfraction == 0:
                raise ZeroDivisionError("Division by zero")
            return Fraction(self._numerator, self._denominator * otherfraction)

    def __rtruediv__(self, otherfraction: "Fraction | int") -> "Fraction":
        """
        Reverse division.

        :param othefractionrfraction: int or Fraction
        :raises ZeroDivisionError: if dividing by zero
        :return: Fraction

        >>> 2 / Fraction(1, 2)
        Fraction(4, 1)
        """
        if self._numerator == 0:
            raise ZeroDivisionError("Division by zero fraction")
        if isinstance(otherfraction, Fraction):
            return Fraction(
                otherfraction._numerator * self._denominator,
                otherfraction._denominator * self._numerator,
            )
        else:
            return Fraction(otherfraction * self._denominator, self._numerator)


if __name__ == "__main__":
    import doctest

    _ = doctest.testmod()
