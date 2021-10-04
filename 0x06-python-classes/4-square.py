#!/usr/bin/python3
"""Square class with private instance attribute"""


class Square:
    """Instantiate square size with a private attribute."""

    def __init__(self, size=0):
        """Initialize square with @size (with fallback value of 0).

        Args:
            self (object): Refers to the object instance
            size (int): A private instance attribute of self
        """
        self.__size = size
        return

    def area(self):
        """Calculate the area of square using size.

        Args:
            self (object): Refers to the object instance

        Returns:
            Square area according to @size private instance attribute
        """
        return pow(self.__size, 2)

    @property
    def size(self):
        """Return the size of square.

        Args:
            self (object): Refers to the object instance

        Returns:
            The private attribute 'size'
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size according to passed argument 'value'.

        Args:
            self (object): Refers to the object instance

        Returns:
            None
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")
        return
