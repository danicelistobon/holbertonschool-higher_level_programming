#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        cp_matrix = []
        for i in matrix:
            cp_matrix.append([x ** 2 for x in i])
        return cp_matrix
