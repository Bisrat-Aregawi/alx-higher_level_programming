#!/usr/bin/python3
"""Defines save_to_json_file function."""
import json


def save_to_json_file(my_obj, filename):
    """Write a py object to a file as a string.

    Args:
        my_obj (obj): Object to serialize
        filename (str): Name of file to write to

    Returns:
        None
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)

    return None
