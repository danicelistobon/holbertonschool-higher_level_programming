#!/usr/bin/python3
"""Module to return True or False
    Args:
        obj (any type): object
        a_class (any type): specified class
"""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance of the specified
        class; otherwise False
    """
    return type(obj) is a_class
