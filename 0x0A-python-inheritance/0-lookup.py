#!/usr/bin/python3
"""Defines an attribute returner function."""


def lookup(obj):
    """Return all attributes and methods of an object.

    Args:
        obj (object): an object parameter

    Returns:
        a list of all attributes and methods of @obj
    """
    return dir(obj)
