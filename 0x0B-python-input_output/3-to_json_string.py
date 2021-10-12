#!/usr/bin/python3
"""Defines to_json_string function."""
import json


def to_json_string(my_obj):
    """Serialize @my_obj to JSON string.

    Args:
        my_obj (object): Object passed to be serialized

    Returns:
        JSON representation of @my_obj
    """
    return (json.dumps(my_obj))
