#!/usr/bin/python3
"""Module to return True or False
    Args:
        obj (any type): object
        a_class (any type): specified class
"""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class; otherwise False
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
