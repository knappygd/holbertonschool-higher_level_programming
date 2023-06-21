#!/usr/bin/python3
"""
Class that raises an exeption
"""
BaseGeometry = __import__('7-rectangle').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Inherits from BaseGeometry and instantiates
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
