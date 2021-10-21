#!/usr/bin/python3
"""Module defines `MyInt` class."""


class MyInt(int):
    """`MyInt` class inherits `int` superclass."""

    def __init__(self, value):
        self.__value = value
        return None

    def __eq__(self, other):
        if self.__value == other:
            return self.__value != other

    def __ne__(self, other):
        if self.__value == other:
            return self.__value == other

    def __str__(self):
        return f"{self.__value}"
