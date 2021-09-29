#!/usr/bin/python3
"""Square class with private instance attribute."""


class Square:
    """Instantiate square size with a private attribute."""

    def __init__(self, size=0):
        """Initialize object with @size (with a fallback valaue of 0).

        Args:
            self (object): Refers to the object instance
            size (int): A private instance attribute of self
        """
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
        self.__size = size
