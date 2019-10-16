#!/usr/bin/python3
"""Module to inherit from BaseGeometry
    Args:
        width (int): rectangle width
        height (int): rectangle height
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """Initializes Rectangle class
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """Area of a rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """Returns rectangle description
        """
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)
