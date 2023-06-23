#!/usr/bin/python3
"""
Returns a Pascal Triangle
"""


def pascal_triangle(n):
    """
    Returns a Pascal Triangle up to n iterations
    """

    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        last = triangle[-1]
        row = [1]
        for i in range(len(last) - 1):
            row.append(last[i] + last[i + 1])
        row.append(1)
        triangle.append(row)
    return triangle
