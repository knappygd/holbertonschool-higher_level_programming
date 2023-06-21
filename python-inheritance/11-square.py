#!/usr/bin/python3
"""
Class that raises an exeption
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Inherits from BaseGeometry and instantiates

    Args:
        Rectangle (BaseGeometry): Is a class
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
