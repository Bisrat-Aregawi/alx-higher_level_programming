#!/usr/bin/python3
"""Defines 'say_my_name function."""


def say_my_name(first_name, last_name=""):
    """Output given name followed by last name.

    Args:
        first_name (str): Given name
        last_name (str, optional): Last name

    Returns:
        None

    Raises:
        TypeError: in conditions of either first_name or last_name name are not
                    a string (is raised if both are not a string aswell).
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
    return None
