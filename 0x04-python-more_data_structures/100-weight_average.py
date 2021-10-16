#!/usr/bin/python3
"""Defines weight_average function."""


def weight_average(my_list=[]):
    """Gives the weighted average of a given list.

    Calculates weighted average by multiplying every element's of an element
    (i.e. tuple) with one another.

    Args:
        my_list (list): List of tuples.

    Returns:
        Weighted average
    """
    if my_list:
        sum = 0
        divider = 0
        for elem in my_list:
            x, y = elem[0], elem[1]
            divider += y
            sum += x * y
        return sum / divider
    return 0
