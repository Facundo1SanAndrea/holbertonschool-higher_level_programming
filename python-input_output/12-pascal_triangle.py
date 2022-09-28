#!/usr/bin/python3
"""list of lists of integers representing the Pascal’s triangle o"""


def pascal_triangle(n):
    """Return pascal triangle"""
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        triangle.append([1])
        for x in range(1, i + 1):
            try:
                triangle[i].append(triangle[i - 1][x - 1] + triangle[i - 1][x])
            except IndexError:
                triangle[i].append(1)
                continue
    return triangle
