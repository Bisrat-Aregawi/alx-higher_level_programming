#!/usr/bin/python3
"""Defines load_from_json_file function."""
import json


def load_from_json_file(filename):
    """Create an object from the JSON file @filename.

    Args:
        filename (str): String representation of an object

    Returns:
        None
    """
    with open(filename) as file:
        obj_frm_json = json.loads(file.read())

    return obj_frm_json
