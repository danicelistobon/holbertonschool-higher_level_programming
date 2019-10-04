#!/usr/bin/python3
"""Module to add 2 integers (a + b)
    Args:
        a (int or float): first number
        b (int or float): second number
"""


def add_integer(a, b=98):
    """Function that adds 2 integers
        Return: result of the sum (a + b)
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
