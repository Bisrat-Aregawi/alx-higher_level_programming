#!/usr/bin/python3
"""Defines adder function."""


def add_integer(a, b=98):
    """Add a and b together.

    Args:
        a (int): First integer
        b (int, optional): Second integer

    Returns:
        The sum of a and b

    Raises:
        TypeError: either a or b are not integers
    """
    if isinstance(a, int) or isinstance(a, float):
        if isinstance(b, int) or isinstance(b, float):
            return int(a) + int(b)
        raise TypeError("b must be an integer")
    raise TypeError("a must be an integer")

if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/0-add_integer.txt")
