#!/usr/bin/python3
"""Defines 'is_same_class' function."""


def is_same_class(obj, a_class):
    """Return truthful values if @obj is an instance of @a_class.

    Args:
        obj (object): Refers to instantiated object
        a_class (type): Class in which to search @obj

    Returns:
        True if @obj is instance of @a_class, False otherwise
    """
    return type(obj) is a_class
