#!/usr/bin/python3
"""Module to inherit from list and print it
    Args:
        list (int): integer list
"""


class MyList(list):
    """Class that inherits from list
    """

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
