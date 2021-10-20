#!/usr/bin/python3
"""Define a test class from unittest module."""


import unittest
import sys

sys.path.append("../")
max_integer = __import__("6-max_integer").max_integer

class TestMaxInteger(unittest.TestCase):
    """Class to test function 'max_integer'."""

    def test_max_integer(self):
        """Test 'max_integer' function."""
        self.assertEqual(max_integer([1, 2, 3]), 3)

        self.assertEqual(max_integer(), None)

        with self.assertRaises(TypeError):
            max_integer([1, 2, 'a'])

        self.assertEqual(max_integer([3, 2, 1]), 3)

        self.assertEqual(max_integer([1, 3, 2]), 3)

        self.assertEqual(max_integer([-1, 3, 2]), 3)

        self.assertEqual(max_integer([-1, -2, -3]), -1)

        self.assertEqual(max_integer([3]), 3)
        return None
