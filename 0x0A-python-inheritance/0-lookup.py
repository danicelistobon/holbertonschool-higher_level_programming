#!/usr/bin/python3
"""Module to return a list
    Args:
        obj (any type): object
"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object
    """
    return dir(obj)
