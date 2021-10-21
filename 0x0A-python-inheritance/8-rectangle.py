#!/usr/bin/python3
"""Module defines `Rectangle` class."""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """`Rectangle` class inheriting `BaseGeometry` superclass."""

    def __init__(self, width, height):
        """Defines @width and @height upon instantiation.

        Args:
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
