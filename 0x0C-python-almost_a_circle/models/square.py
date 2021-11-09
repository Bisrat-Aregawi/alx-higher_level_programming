#!/usr/bin/python3
"""Defines 'Square' subclass."""
from models import rectangle


class Square(rectangle.Rectangle):
    """Initializes Square objects with attributes.

    It defnies mandatory @size and optional @x & @y coordinates upon object
    instantiation and defines instance methods to get and set them
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Define attributes for square object.

        Args:
            self (object): Refers to object instantiated
            size (int): Size of Square
            x (int, optional): Horizontal measurement
            y (int, optional): Vertical measurement

        Returns:
            None
        """
        super().__init__(size, size, x, y, id)
        return None

    @property
    def size(self):
        """Return size of square.

        Args:
            self (object): Refers to object instantiated

        Returns:
            The private attribute 'size'
        """
        return super().width

    @size.setter
    def size(self, value):
        """Sets the @width and @height attribs to @value

        Args:
            self (object): Refers to object instantiated
            value (int): value to set @width & @height

        Returns:
            None
        """
        self.width = value
        self.height = value
        return None

    def __str__(self):
        """Display object representing string.

        Args:
            self (object): Refers to object instantiated

        Returns:
            String representation of square object
        """
        string = "[Square] ({}) {}/{}".format(self.id, self.x, self.y)
        string += " - {}".format(self.size)
        return string

    def update(self, *args, **kwargs):
        """Update attributes of Square object.

        Args:
            First element of @args is 'id'
            Second element of @args is 'width'
            Third element of @args is 'height'
            Fourth element of @args is 'x'
            Fifth element of @args is 'y'

        Returns:
            None
        """
        arg_position = 0
        if len(args) != 0:
            for elem in args:
                if arg_position == 0:
                    self.id = elem
                elif arg_position == 1:
                    self.size = elem
                elif arg_position == 2:
                    self.x = elem
                elif arg_position == 3:
                    self.y = elem
                arg_position = arg_position + 1
        else:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
        return None
    pass
