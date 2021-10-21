#!/usr/bin/python3
"""Module defines `add_attribute` function."""


def add_attribute(obj, attrib, value):
    """Adds @attrib to obj if possible.

    Args:
        obj (object): Object to add @attrib into
        attrib (str): Attribute name
        value (str, int, etc ...): Value of @attrib

    Returns:
        None
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    obj.__setattr__(attrib, value)
    return None
