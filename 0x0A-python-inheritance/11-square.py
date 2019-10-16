#!/usr/bin/python3
"""Module to inherit from Rectangle
    Args:
        size (int): square size
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle
    """

    def __init__(self, size):
        """Initializes Square class
        """
        super().__init__(size, size)
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        """Area of a square
        """
        return self.__size ** 2

    def __str__(self):
        """Returns square description
        """
        return '[Square] {}/{}'.format(self.__size, self.__size)
