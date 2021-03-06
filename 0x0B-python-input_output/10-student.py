#!/usr/bin/python3
"""Contains the clas 'Student'."""


class Student:
    """Student type."""

    def __init__(self, first_name, last_name, age):
        """Initialize the student object."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dict representation of object with specific attribs."""
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for a in attrs:
            try:
                new_dict[a] = self.__dict__[a]
            except:
                pass
        return new_dict
