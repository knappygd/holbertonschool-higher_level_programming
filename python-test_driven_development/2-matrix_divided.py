#!/usr/bin/python3

def matrix_divided(matrix, div):
    for i in matrix:
        for j in matrix[i]:
            if not isinstance(matrix[i][j], int)\
                    and not isinstance(matrix[i][j], float):
                raise TypeError("matrix must be a matrix (list of lists) \
                                of integers/floats")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new = matrix.copy()
    for i in range(len(matrix)):
        new[i] = list(map(lambda x: round((x / div), 2), matrix[i]))
    return new
