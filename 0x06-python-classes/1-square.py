#!/usr/bin/python3
"""Square class with private instance attribute."""


class Square:
    """Instantiate square size with a private attribute."""

    def __init__(self, size):
        """Initialize object with @size object attribute.

        Args:
            self (object): Refers to the object instance
            size (int): A private instance attribute of self
        """
        self.__size = size
