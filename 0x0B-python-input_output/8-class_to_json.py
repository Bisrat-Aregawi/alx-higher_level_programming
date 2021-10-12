#!/usr/bin/python3
"""Defines class_to_json function."""


def class_to_json(obj):
    """Return a dictionary description for JSON serialization.

    Args:
        obj (object): Object to list builtins

    Returns:
        Dictionary description of @obj
    """
    return obj.__dict__
