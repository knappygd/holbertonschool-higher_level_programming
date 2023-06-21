#!/usr/bin/python3
"""
Class that raises an exeption
"""


class BaseGeometry:
    """
    Raises an Exception with the message area() is not implemented
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise TypeError("{} must be greater than 0".format(name))
