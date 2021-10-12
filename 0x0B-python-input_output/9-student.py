#!/usr/bin/python3
"""Defines the class Student."""


class Student:
    """Representation of a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize Students' instances."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        return None

    def to_json(self):
        """Return a dict representation of the object."""
        return self.__dict__
