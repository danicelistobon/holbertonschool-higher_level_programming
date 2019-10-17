#!/usr/bin/python3
"""Module to append a string at the end of a text file
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8) and returns the
        number of characters added
    """

    with open(filename, 'a', encoding='utf-8') as new_file:
        new_file.write(text)
    return len(text)
