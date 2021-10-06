#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Initializes rectangle objects with width and height attribs.

    It defines optional width and height private instance attributes upon
    object creation and defines instance methods to get and set them. In
    addition It has public instance methods to get the area and perimeter. An
    additional 'magic' method __str__ is used to showcase the rectangle in
    terminal.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Declare the width and height of rectangle object upon creation.

        Args:
            self (Rectangle's object): Refers to instantiated object
            width (int, optional): Width of rectangle object
            height (int, optional): Height or rectangle object

        Returns:
            None
        """
        handle_exception(width, "width")
        handle_exception(height, "height")
        Rectangle.number_of_instances += 1
        self.__width = width
        self.__height = height
        return None

    @property
    def width(self):
        """Getter method to retrieve the width.

        Args:
            self (Rectangle's object): Refers to instantiated object

        Returns:
            width private instance attribute
        """
        return self.__width

    @property
    def height(self):
        """Getter method to retrieve the height.

        Args:
            self (Rectangle's object): Refers to instantiated object

        Returns:
            height private instance attribute
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Setter method for the width.

        Args:
            self (Rectangle's object): Refers ti instantiated object
            value (int): Value to replace width private attribute

        Returns:
            None
        """
        handle_exception(value, "width")
        self.__width = value
        return None

    @height.setter
    def height(self, value):
        """Setter method for the height.

        Args:
            self (Rectangle's object): Refers to instantiated object
            value (int): Value to replace height private attribute

        Returns:
            None
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

    def __str__(self):
        """Builtin 'magic' method to represent Rectangle's objects.

        Args:
            self (Rectangle's object): Refers to instantiated object

        Returns:
            object representation with '#' character on the terminal
        """
        rect = ""
        if self.__width == 0 or self.__height == 0:
            return rect
        for i in range(self.__height):
            rect += "#" * self.__width
            rect += "\n"
        return rect[:-1]

    def __repr__(self):
        """Builtin 'magic' method which returns a command string.

        Args:
            self (Rectangle's object): Refers to instantiated object

        Returns:
            string of a py expression to create objects usig 'eval'
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Builtin 'magic' method executes when 'del' is called on an object

        Args:
            self (Rectangle's object): Refers to instantiated object

        Returns:
            None
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
        return None

    pass


def handle_exception(value, attrib):
    """Raise exceptions according to defined conventions.

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
