#!/usr/bin/python3
"""Module defines a class Square to create square objects."""


class Square:
    """Instantiates objects which are square and have private attribs.

    Creates objects by taking the size data. It provides its objects with
    public methods. namely area, my_print, getter, and setter methods.
    """
    def __init__(self, size=0):
        """Initializes objects of 'Square' with @size.

        Args:
            self (Square's object): Refers to the object instance
            size (int, optional): Private instance attribute of created object

        Returns:
            None
        """
        self.__size = size
        return None

    @property
    def size(self):
        """Returns @size private attribute of object.

        Args:
            self (Square's object): Refers to the object instance

        Returns:
            @size attribute of instantiated object
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Updates @size private attribute of object.

        Args:
            self (Square's object): Refers to the object instance
            value (int): The value we replace @size with

        Returns:
            None

        Raises:
            ValueError: The value passed is < 0
            TypeError: The value passed is not an integer
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")
        return None

    def area(self):
        """Calculates and gives the area.

        Uses the private instance attribute '__size' to calculate
        the area of the square object

        Args:
            self (Square's object): Refers to the obect instance

        Returns:
            Area calculated from '__size' of the square object
        """
        return pow(self.__size, 2)

    def my_print(self):
        """Prints the character # to represent the square in terminal.

        Args:
            self (Square's object): Refers to the object instance

        Returns:
            None
        """
        if self.__size == 0:
            print()
            return None
        for i in range(self.__size):
            print("#" * self.__size)

        return None
