#!/usr/bin/python3
"""Define a square"""


class Square:
    """
    Initialize a square

    Args:
        size (int): The size of the square
    """
    def __init__(self, size=0):
        if isinstance(size, int) == False:
            raise TypeError()
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
