#!/usr/bin/python3
"""Defines an inheriter class MyList."""


class MyList(list):
    """Inherits from the superclass 'list'."""

    def print_sorted(self):
        """Print a sorted list.

        Args:
            self (MyList's object): Refers to instantiated object

        Returns:
            None
        """
        local_list = self[:]
        local_list.sort()
        print(local_list)
        return None
