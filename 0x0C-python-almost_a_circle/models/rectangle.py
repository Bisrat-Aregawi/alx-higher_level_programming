#!/usr/bin/python3
"""Defines 'Rectangle' class."""
from models import base


class Rectangle(base.Base):
    """Inherits from superclass 'Base'."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Define attributes of rectangle object.

        Args:
            self (object): Refers to object instantiated
            width (int): Width of rectangle
            height (int): Height of rectangle
            x (int, optional): Horizontal measurement
            y (int, optional): Vertical measurement

        Returns:
            None
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        return None

    @property
    def width(self):
        """Return width of square.

        Args:
            self (object): Refers to object instantiated

        Returns:
            The private attribute 'width'
        """
        return self.__width

    @property
    def height(self):
        """Return height of square.

        Args:
            self (object): Refers to object instantiated

        Returns:
            The private attribute 'height'
        """
        return self.__height

    @property
    def x(self):
        """Return x coordinate of square.

        Args:
            self (object): Refers to object instantiated

        Returns:
            The private attribute 'x'
        """
        return self.__x

    @property
    def y(self):
        """Return y coordinate of square.

        Args:
            self (object): Refers to object instantiated

        Returns:
            The private attribute 'y'
        """
        return self.__y

    @width.setter
    def width(self, value):
        """Set the width according to passed 'value'

        Args:
            self (object): Refers to object instantiated
            value (int): Value to assign to 'width' private attribute

        Returns:
            None
        """
        self.__width = value
        return None

    @height.setter
    def height(self, value):
        """Set the height according to passed 'value'

        Args:
            self (object): Refers to object instantiated
            value (int): Value to assign to 'height' private attribute

        Returns:
            None
        """
        self.__height = value
        return None

    @x.setter
    def x(self, value):
        """Set the x coordinate according to passed 'value'

        Args:
            self (object): Refers to object instantiated
            value (int): Value to assign to 'x' private attribute

        Returns:
            None
        """
        self.__x = value
        return None

    @y.setter
    def y(self, value):
        """Set the y coordinate according to passed 'value'

        Args:
            self (object): Refers to object instantiated
            value (int): Value to assign to 'y' private attribute

        Returns:
            None
        """
        self.__y = value
        return None
