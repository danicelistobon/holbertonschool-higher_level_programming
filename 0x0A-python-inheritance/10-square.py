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
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """Area of a square
        """
        return self.__size ** 2
