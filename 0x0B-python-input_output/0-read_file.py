#!/usr/bin/python3
"""Defines read_file function."""


def read_file(filename=""):
    """Perform a print to stdout of a file.

    Args:
        filename (str): String representation of file name to read

    Returns:
        None
    """
    with open(filename) as file:
        text = file.read()
    print(text, end="")
    return None
