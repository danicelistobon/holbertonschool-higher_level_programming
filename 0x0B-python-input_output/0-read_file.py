#!/usr/bin/python3
"""Module to read a text file and print it
"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout
    """

    with open(filename, 'r', encoding='utf-8') as new_file:
        print(new_file.read(), end='')
