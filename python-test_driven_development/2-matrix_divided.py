#!/usr/bin/python3

def matrix_divided(matrix, div):
    new = matrix.copy()
    for i in range(len(matrix)):
        new[i] = list(map(lambda x: x / div, matrix[i]))
    return new
