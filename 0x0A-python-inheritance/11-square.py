#!/usr/bin/python3
"""Module defines `Square` class."""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """`Square` class inherits from `Rectangle` superclass."""

    def __init__(self, size):
        """Define @size upon instantiation.

        Args:
            self (object): Refers to object instantiated
            size (int): Width or Rectangle object

        Returns:
            None
        """
        if super().integer_validator("size", size) is None:
            self.__size = size
        super().__init__(size, size)
        return None

    def area(self):
        """Area function to return the area of square object.

        Args:
            self (object): Refers to object instantiated

        Returns:
            Square of self.__size
        """
        return pow(self.__size, 2)

    def __str__(self):
        """Add functionality to print return value below.

        Args:
            self (object): Refers to object instantiated

        Returns:
            concise formated string about object
        """
        return f"[Square] {self.__size}/{self.__size}"

    def __repr__(self):
        """Add functionality to return the return value below

        Args:
            self (object): Refers to object instantiated

        Returns:
            concise formated string about object
        """
        return f"[Square] {self.__size}/{self.__size}"
