#!/usr/bin/python3
"""Defines 'inherits_from' function."""


def inherits_from(obj, a_class):
    """Returns Truth about @obj's origins.

    Args:
        obj (object): Potential object of @a_class
        a_class (class): Potential class for @obj

    Returns:
        True if obj is an instance of a class that inherits from @a_class
        False otherwise
    """
    if type(obj) == a_class:
        return False
    return isinstance(obj, a_class)
