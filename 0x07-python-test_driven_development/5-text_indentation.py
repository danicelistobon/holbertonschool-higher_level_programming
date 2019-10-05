#!/usr/bin/python3
"""Module to prints a text with 2 new lines after each of these
    characters: ., ? and :
    Args:
        text (str): string
"""


def text_indentation(text):
    """Function that prints a text
        Return: printed text
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    for i in range(len(text)):
        if text[i] == ' ' and text[i + 1] == ' ':
            continue
        if text[i] is ' ' and text[i - 1] is '.':
            continue
        if text[i] is ' ' and text[i - 1] is '?':
            continue
        if text[i] is ' ' and text[i - 1] is ':':
            continue
        if text[i] is ' ' and text[i - 1] is ' ':
            continue
        print(text[i], end='')
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print()
            print()
