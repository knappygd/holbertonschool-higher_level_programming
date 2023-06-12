#!/usr/bin/python3
"""Define a square"""


class Square:
    """
    Initialize a square

    Args:
        size (int): The size of the square
    """
    def __init__(self, size):
        if isinstance(size, int) == False:
            raise TypeError()
        elif size < 0:
            raise ValueError()
        self.__size = size
