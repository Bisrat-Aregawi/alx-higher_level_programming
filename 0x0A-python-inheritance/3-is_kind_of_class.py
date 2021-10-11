#!/usr/bin/python3
"""Defines is_kind_of_class function."""


def is_kind_of_class(obj, a_class):
    """Return truthful values if @obj is instance of @a_class.

    a_class can be a super super class of obj and the function must return true
    in that situation aswell.

    Args:
        obj (object): Refers to instantiated object
        a_class (type): The class in which to find @obj

    Returns:
        True if @obj is instance of @a_class, False otherwise
    """
    return isinstance(obj, a_class)
