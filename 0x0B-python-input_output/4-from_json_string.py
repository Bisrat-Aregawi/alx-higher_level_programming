#!/usr/bin/python3
"""Defines from_json_string function."""
import json


def from_json_string(my_str):
    """deserializes @my_str to a JSON object.

    Args:
        my_str (str): String to deserialize

    Returns:
        A python data structure represented by @my_str
    """
    return json.loads(my_str)
