#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Initializes rectangle objects with width and height attribs.

    It defines optional width and height private instance attributes upon
    object creation and defines instance methods to get and set them. In
    addition It has public instance methods to get the area and perimeter.
    """

    def __init__(self, width=0, height=0):
        """Declare the width and height of rectangle object upon creation.

        Args:
            self (Rectangle's object): Refers to instantiated object
            width (int, optional): Wdith of rectangle object
            height (int, optional): Height of rectangle object

        Returns:
            None
        """
        handle_exception(width, "width")
        handle_exception(height, "height")
        self.__width = width
        self.__height = height
        return None

    @property
    def width(self):
        """Retrieve the width attribute of rectangle object.

        Args:
            self (Rectangle's object): Refers to instantiated object

        Returns:
            width private instance attribute
        """
        return self.__width

    @property
    def height(self):
        """Retrieve the height attribute of rectangle object.

        Args:
            self (Rectangle's object): Refers ot instantiated object

        Returns:
            height private instance attribute
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Update the width attribute of rectangle object.

        Args:
            self (Rectangle's object): Refers to instantiated object
            value (int): Value to replace width private attribute

        Returns:
            None

        Raises:
            ValueError: width must be an integer
            TypeError: width must be >= 0
        """
        handle_exception(value, "width")
        self.__width = value
        return None

    @height.setter
    def height(self, value):
        """Update the height attribute of rectangle object.

        Args:
            self (Rectangle's object): Refers to instantiated object
            value (int): Value to replace width private attribute

        Returns:
            None

        Raises:
            ValueError: height must be an integer
            TypeError: height must be >= 0
        """
        handle_exception(value, "height")
        self.__height = value
        return None

    def area(self):
        """Calculate the area of rectangle.

        Args:
            self (Rectangle's object): Refers to instantiated object

        Returns:
            Area of rectangle object
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of rectangle.

        Args:
            self (Rectangle's object): Refers to instantiated object

        Returns:
            Perimeter of rectangle object
        """
        w, h = self.__width, self.__height
        return 0 if w == 0 or h == 0 else 2 * w + 2 * h
    pass


def handle_exception(value, attrib):
    """Respond according to predefined conventions.

    This function will test @value against predefined conventions and raise
    exceptions according to those conventions being satisfied or not.

    Args:
        value (int): Value to be examined
        attrib (str): Private instance attribute with value @value

    Returns:
        None

    Raises:
        ValueError: value is < 0
        TypeError: value is not an integer
    """
    if isinstance(value, int):
        if value < 0:
            raise ValueError("{} must be >= 0".format(attrib))
        else:
            return None
    else:
        raise TypeError("{} must be an integer".format(attrib))
