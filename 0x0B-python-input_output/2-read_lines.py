#!/usr/bin/python3
"""Module to read n lines of a text file
"""


def read_lines(filename="", nb_lines=0):
    """Reads n lines of a text file (UTF8) and prints it to stdout
    """

    count = 0

    with open(filename, 'r', encoding='utf-8') as new_file:
        for line in new_file:
            if count < nb_lines or nb_lines <= 0:
                print(line, end='')
                count += 1
