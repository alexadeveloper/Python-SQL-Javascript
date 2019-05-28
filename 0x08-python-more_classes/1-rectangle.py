#!/usr/bin/python3
"""Define a class"""


class Rectangle:
    """ define a rectangle"""

    def __init__(self, width, height):
        """init the rectangle
        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    @property
    def height(self):
        """return the height"""

        return self.__height

    @height.setter
    def height(self, value):
        """set the height"""

        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """return the width"""

        return self.__width

    @width.setter
    def width(self, value):
        """set the width"""

        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
