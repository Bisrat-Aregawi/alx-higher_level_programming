#!/usr/bin/python3
"""Module defines print_square function."""


def print_square(size):
    """Draw a square of @size units

    Args:
        size (int): Size of square to print

    Returns:
        None
    """
    if isinstance(size, int):
        if size < 0:
            raise ValueError("size must be >= 0")
        for h in range(size):
            print("#" * size)
    else:
        raise TypeError("size must be an integer")
