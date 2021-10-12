#!/usr/bin/python3
"""Defines write_file function."""


def write_file(filename="", text=""):
    """Write to a file with UTF-8 encoding.

    Args:
        filename (str, optional): Name of file to create or overwrite
        text (str, optional): Name of text to insert in to @filename

    Returns:
        Character count inside @filename
    """
    with open(filename, encoding="UTF-8", mode="w") as file:
        char_count = file.write(text)
    return char_count
