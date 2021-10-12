#!/usr/bin/python3
"""Defines append_write function."""


def append_write(filename="", text=""):
    """Appends to @filename contents of @text.

    Args:
        filename (str, optional): File name
        text (str, optional): Content to append in @filename

    Returns:
        Number of characters appended
    """
    with open(filename, encoding="UTF-8", mode="a") as file:
        char_count = file.write(text)
    return char_count
