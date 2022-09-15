#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    if matrix is None:
        return

    another_matrix = []
    for x in range(0, len(matrix)):
        squares = list(map(lambda x: x**2, matrix[x]))
        another_matrix.append(squares)
    return another_matrix
