#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for line in (matrix):
        for row in (line):
            print("{:d}".format(row), end="")
            if (row != line[-1]):
                print(" ", end="")
        print()
