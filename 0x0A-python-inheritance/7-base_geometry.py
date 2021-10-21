#!/usr/bin/python3
"""Module defines 'BaseGeometry' class."""


class BaseGeometry:
    """'BaseGeometry' class."""

    def area(self):
        """'area' method.

        Args:
            self (object): refers to instantiated object

        Returns:
            None
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """'integer_validator' method.

        Args:
            self (object): refers to instantiated object
            name (str): name of integer
            value (int): integer referenced by @name

        Returns:
            None

        Raises:
            TypeError: If @value is not an integer
            ValueError: If @value is less than or equal to zero
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
