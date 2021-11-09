#!/usr/bin/python3
"""Defines 'Square' subclass."""
from models import rectangle


class Square(rectangle.Rectangle):
    """Initializes Square objects with attributes.

    It defnies mandatory @size and optional @x & @y coordinates upon object
    instantiation and defines instance methods to get and set them
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Define attributes for square object.

        Args:
            self (object): Refers to object instantiated
            size (int): Size of Square
            x (int, optional): Horizontal measurement
            y (int, optional): Vertical measurement

        Returns:
            None
        """
        super().__init__(size, size, x, y, id)
        return None

    @property
    def size(self):
        """Return size of square.

        Args:
            self (object): Refers to object instantiated

        Returns:
            The private attribute 'size'
        """
        return super().width

    @property
    def x(self):
        """Return x coordinate of square.

        Args:
            self (object): Refers to object instantiated

        Returns:
            The private attribute 'x'
        """
        return super().x

    @property
    def y(self):
        """Return y coordinate of square.

        Args:
            self (object): Refers to object instantiated

        Returns:
            The private attribute 'y'
        """
        return super().y

    def __str__(self):
        """Display object representing string.

        Args:
            self (object): Refers to object instantiated

        Returns:
            String representation of square object
        """
        string = f"[Square] ({self.id}) {self.x}/{self.y}"
        string += f" - {self.size}"

        return string
