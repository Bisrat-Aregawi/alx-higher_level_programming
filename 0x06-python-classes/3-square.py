#!/usr/bin/python3
"""Square class with private instance attribute."""


class Square:
    """Instantiate square size with a private attribute."""

    def __init__(self, size=0):
        """Initialize object with @size (with fallback value of 0).

        Args:
            self (object): Refers to the object instance
            size (int): A private instance attribute of self
        """
        self.__size = size
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
        return

    def area(self):
        """Calculate the area of square using size.

        Args:
            self (object): Refers to the object instance

        Returns:
            Square area according to @size private instance attribute
        """
        return pow(self.__size, 2)
