#!/usr/bin/python3
"""Defines a class Square to create square objects with coordinates."""


class Square:
    """Defines private instance attributes for a square in 2D plane.

    Creates square objects with 2D coordinates. It provides its objects
    with public methods namely area, my_print, size, position, getter,
    and setter methods.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes objects of 'Square' with @size.

        Args:
            self (Square's object): Refers to the object instance
            size (int, optional): Private instance attribute of created object

        Returns:
            None
        """
        self.__size = size
        if isinstance(position, tuple) and len(position) == 2:
            for elem in position:
                if not isinstance(elem, int) or elem < 0:
                    raise ValueError("position must be a tuple" +
                                     " of 2 positive integers")
            self.__position = position
        else:
            raise ValueError("position must be a tuple of 2 positive integers")
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

    @property
    def position(self):
        """Returns @position private attribute of object.

        Args:
            self (Square's object): Refers to the object instance

        Returns:
            @position attribute of instantiated object
        """
        return self.__position

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

    @position.setter
    def position(self, value):
        """Updates @position private attribute of object.

        Args:
            self (Square's object): Refers to the object instance
            value (int): The value we replace @position with

        Returns:
            None

        Raises:
            ValueError: The value passed is < 0
            TypeError: The value passed is not an integer
        """
        if isinstance(value, tuple):
            if len(value) != 2:
                raise TypeError("position must be a tuple of \
                                2 positive integers")
            else:
                self.__position = position
        else:
            raise ValueError("position must be a tuple")
        return None

    def area(self):
        """Calculates an gives the area.

        Uses the private intsance attribute '__size' to calculate
        the area of the square object

        Args:
            self (Square's object): Refers to the object instance

        Returns:
            Area calculated from '__size' of the square object
        """
        return pow(self.__size, 2)

    def my_print(self):
        """Prints the character '#' to represent the square in terminal.

        Args:
            self (Square's object): Refers to the object instance

        Returns:
            None
        """
        if self.__size == 0:
            print()
            return None
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
