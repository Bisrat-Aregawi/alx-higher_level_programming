#!/usr/bin/python3
"""Defines 'Rectangle' class."""
from models import base


class Rectangle(base.Base):
    """Iniializes rectangle objects with attributes.

    It defines mandatory width & height and optional x & y coordinates upon
    object creation and defines instance methods to get and set them
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Define attributes of rectangle object.

        Args:
            self (object): Refers to object instantiated
            width (int): Width of rectangle
            height (int): Height of rectangle
            x (int, optional): Horizontal measurement
            y (int, optional): Vertical measurement

        Returns:
            None
        """
        handle_exception(width, "width", 1)
        handle_exception(height, "height", 1)
        handle_exception(x, "x", 0)
        handle_exception(y, "y", 0)
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        return None

    @property
    def width(self):
        """Return width of rectangle.

        Args:
            self (object): Refers to object instantiated

        Returns:
            The private attribute 'width'
        """
        return self.__width

    @property
    def height(self):
        """Return height of rectangle.

        Args:
            self (object): Refers to object instantiated

        Returns:
            The private attribute 'height'
        """
        return self.__height

    @property
    def x(self):
        """Return x coordinate of rectangle.

        Args:
            self (object): Refers to object instantiated

        Returns:
            The private attribute 'x'
        """
        return self.__x

    @property
    def y(self):
        """Return y coordinate of square.

        Args:
            self (object): Refers to object instantiated

        Returns:
            The private attribute 'y'
        """
        return self.__y

    @width.setter
    def width(self, value):
        """Set the width according to passed 'value'.

        Args:
            self (object): Refers to object instantiated
            value (int): Value to assign to 'width' private attribute

        Returns:
            None
        """
        handle_exception(value, "width", 1)
        self.__width = value
        return None

    @height.setter
    def height(self, value):
        """Set the height according to passed 'value'.

        Args:
            self (object): Refers to object instantiated
            value (int): Value to assign to 'height' private attribute

        Returns:
            None
        """
        handle_exception(value, "height", 1)
        self.__height = value
        return None

    @x.setter
    def x(self, value):
        """Set the x coordinate according to passed 'value'.

        Args:
            self (object): Refers to object instantiated
            value (int): Value to assign to 'x' private attribute

        Returns:
            None
        """
        handle_exception(value, "x", 0)
        self.__x = value
        return None

    @y.setter
    def y(self, value):
        """Set the y coordinate according to passed 'value'.

        Args:
            self (object): Refers to object instantiated
            value (int): Value to assign to 'y' private attribute

        Returns:
            None
        """
        handle_exception(value, "y", 0)
        self.__y = value
        return None

    def area(self):
        """Return the area value of rectangle object.

        Args:
            self (object): Refers to object instantiated

        Returns:
            Area of rectangle object
        """
        return self.__width * self.__height

    def display(self):
        """Display the rectangle object with a # character.

        Draws rectangle with hashtag character '#' to the terminal according to
        the values provided to 'width' and 'height' attrubutes

        Args:
            self (object): Refers to object instantiated

        Returns:
            None
        """
        for i in range(self.__y):
            print("")
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)
        return None

    def __str__(self):
        """Display object representing string.

        Args:
            self (object): Refers to object instantiated

        Returns:
            String representation of rectangle object
        """
        string = "[Rectangle] ({}) {}/{}".format(self.id, self.__x, self.__y)
        string += " - {}/{}".format(self.__width, self.__height)

        return string

    def update(self, *args, **kwargs):
        """Update attributes of Rectangle object.

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
                    self.width = elem
                elif arg_position == 2:
                    self.height = elem
                elif arg_position == 3:
                    self.x = elem
                elif arg_position == 4:
                    self.y = elem
                arg_position = arg_position + 1
        else:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
        return None

    pass


def handle_exception(value, attrib, can_be):
    """Respond according to predefined conventions.

    This function will test @value against predefined conventions and raise
    exceptions according to those conventions being satisfied or not

    Args:
        value (int): Value to be examined
        attrib (str): Private instance attribute with value @value

    Returns:
        None

    Raises:
        TypeError: @value is not an integer
        ValueError: @value is either less than or equal to zero
    """
    if isinstance(value, int):
        if value < 0 and can_be == 0:
            raise ValueError("{} must be >= 0".format(attrib))
        elif value <= 0 and can_be == 1:
            raise ValueError("{} must be > 0".format(attrib))
        else:
            return None
    else:
        raise TypeError("{} must be an integer".format(attrib))
