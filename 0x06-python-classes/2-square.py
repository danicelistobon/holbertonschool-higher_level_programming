#!/usr/bin/python3
"""Script that defines a square"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """Initializes Square class

        Args:
            size (int): size of a square
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
