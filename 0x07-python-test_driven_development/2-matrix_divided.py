#!/usr/bin/python3
"""Module to divide all elements of a matrix
    Args:
    matrix (int or float): list of lists of integers or floats
    div (int or float): divisor number
"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix
        Return: new matrix
    """
    new_matrix = []
    length = 0

    error1 = 'matrix must be a matrix (list of lists) of integers/floats'
    error2 = 'Each row of the matrix must have the same size'

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    length = len(matrix[0])

    for r in matrix:
        if not isinstance(r, list):
            raise TypeError(error1)
        if len(r) != length:
            raise TypeError(error2)
        array = []
        for c in r:
            if not isinstance(c, (int, float)):
                raise TypeError(error1)
            array.append(round(c / div, 2))
        new_matrix.append(array)

    return new_matrix
