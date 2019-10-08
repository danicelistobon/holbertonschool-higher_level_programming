#!/usr/bin/python3
"""Module to define a rectangle
    Args:
        width (int): width of a rectangle
        height (int): height of a rectangle
"""


class Rectangle:
    """Rectangle class
    """
    def __init__(self, width=0, height=0):
        """Initializes Rectangle class
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Area of a rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """Perimeter of a rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return ((2 * self.width) + (2 * self.height))
