#!/usr/bin/python3
"""Define a square"""


class Square:

    def __init__(self, size=0):
        """
        Initialize a square

        Args:
            size (int): The size of the square
        """
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size * self.__size
