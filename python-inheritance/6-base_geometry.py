#!/usr/bin/python3
"""
Class that raises an exeption
"""


class BaseGeometry:
    """
    Raises an Exception with the message area() is not implemented
    """

    def area(self):
        raise Exception("area() is not implemented")
