#!/usr/bin/python3
"""
print_square prints a square of a given size
"""


def print_square(size):
    """
    Print a square of <size> dimension
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
