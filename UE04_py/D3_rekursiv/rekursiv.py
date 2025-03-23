from time import time
from pprint import pprint


def M(n: int, rec: int = 0) -> tuple[int, int]:
    """
    :param n: the input integer to run through the McCarthy-91 function
    :return: the computed result and the recursion depth
    """
    if n <= 100:
        m1, rec = M(n + 11, rec + 1)
        m2, rec = M(m1, rec + 1)
        return m2, rec
    else:
        return n - 10, rec


if __name__ == "__main__":
    # The McCarthy-91 function is special because every input from 0-101 will return 91
    t_start = time()
    m_list = [M(i) for i in range(1, 201)]
    m_dict = {i: M(i) for i in range(1, 201)}
    t_end = time()
    print(f"Time elapsed: {t_end - t_start:.6f}s")
    pprint(m_dict)
    # the recursion depth for 1 was the highest
    # takes 0.000736s on my machine
