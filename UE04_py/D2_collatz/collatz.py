import signal
from types import FrameType


def handler(signum: int, frame: FrameType | None) -> TimeoutError:
    """
    :param signum: the signal number
    :param frame: the current stack frame
    :raises TimeoutError: Always raised to indicate a timeout
    """
    raise TimeoutError("Timed out!")


def collatz(n: int, p: int = 3) -> int:
    """
    :param n: non-negative integer
    :param p: non-negative integer (default: 3) for p in the collatz formula
    :return: the next number in the collatz sequence
    """
    if n % 2 == 0:
        return int(n / 2)
    else:
        return p * n + 1


def collatz_sequence(number: int, p: int = 3) -> list[int]:
    """
    :param number: Startzahl
    :param p: non-negative integer (default: 3) for p in the collatz formula
    :return: Collatz Zahlenfolge, resultierend aus n
    >>> collatz_sequence(19)
    [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    if number == 1:
        return [number]
    else:
        return [number, *collatz_sequence(collatz(number, p), p)]


def longest_collatz_sequence(n: int, p: int = 3) -> tuple[int, int]:
    """
    :param number: Startzahl
    :param p: non-negative integer (default: 3) for p in the collatz formula
    :return: Startwert und Länge der längsten Collatz Zahlenfolge deren Startwert <=n ist

    >>> longest_collatz_sequence(100)
    (97, 119)
    """
    max_cl = (0, 0)
    for i in range(n, 0, -1):
        cl = collatz_sequence(i, p)
        if len(cl) > max_cl[1]:
            max_cl = (i, len(cl))

    return max_cl


if __name__ == "__main__":
    assert collatz(1) == 4
    assert collatz(5) == 16
    assert collatz(8) == 4

    assert collatz_sequence(14) == [
        14,
        7,
        22,
        11,
        34,
        17,
        52,
        26,
        13,
        40,
        20,
        10,
        5,
        16,
        8,
        4,
        2,
        1,
    ]
    assert collatz_sequence(7) == [
        7,
        22,
        11,
        34,
        17,
        52,
        26,
        13,
        40,
        20,
        10,
        5,
        16,
        8,
        4,
        2,
        1,
    ]

    assert longest_collatz_sequence(100) == (97, 119)
    assert longest_collatz_sequence(69) == (55, 113)

    for p in range(1, 50):
        _ = signal.signal(signal.SIGALRM, handler)
        _ = signal.alarm(5)
        try:
            _ = collatz_sequence(7, p)
            print(f"Collatz Sequence for n=7 and {p=} worked.")
        except TimeoutError:
            print(f"Collatz Sequence for n=7 and {p=} did not work!")
        except RecursionError:
            print(f"Collatz sequence with n=7 and {p=} reached max recursions!")
    # it seems that increasing p will either increase the length of the
    # sequence OR just get bigger and bigger until it reaces max recursions
