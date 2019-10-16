#!/usr/bin/python3
"""Module to return the number of lines
"""


def number_of_lines(filename=""):
    """Returns the number of lines of a text file
    """

    count = 0

    with open(filename, 'r') as new_file:
        for line in new_file:
            count += 1
    return count
