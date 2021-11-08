#!/usr/bin/python3
"""Module Defines 'Base' class."""


class Base:
    """Class named Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize object with 'id' instance attribute.

        Args:
            self (object): Refers to the object instance
            id (int, optional): Id of created instances
        Returns:
            None
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

        return None
    pass
