#!/usr/bin/python3
"""Module defines `Rectangle` class."""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """`Rectangle` class inheriting `BaseGeometry` superclass."""

    def __init__(self, width, height):
        """Define @width and @height upon instantiation.

        Args
            self (object): Refers to object instantiated
            width (int): Width of Rectangle object
            height (int): Height of Rectangle object

        Returns:
            None
        """
        if super().integer_validator("width", width) is None:
            self.__width = width
        if super().integer_validator("height", height) is None:
            self.__height = height
        return None

    def area(self):
        """Area function to return the area of rectangle object.

        Args:
            self (object): Refers to object instantiated

        Returns:
            Product of self.__width and self.__height
        """
        return self.__width * self.__height

    def __str__(self):
        """Add functionality to print return value below

        Args:
            self (object): Refers to object instantiated

        Returns:
            concise formated string about object
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def __repr__(self):
        """Add functionality to return the return value below

        Args:
            self (object): Refers to object instantiated

        Returns:
            concise formated string about object
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
