#!/usr/bin/python3
"""Class to define a rectangle"""


class Rectangle:
    """Defines a rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.height * 2 + self.width * 2

    def __str__(self):
        rec = ""
        if self.width == 0 or self.height == 0:
            return rec
        for h in range(self.height):
            rec += ("#" * self.width) + "\n"
        return rec[:-1]

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
