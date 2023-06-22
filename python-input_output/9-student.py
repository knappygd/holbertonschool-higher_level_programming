#!/usr/bin/python3
"""
Return the dict description for JSON of an object
"""


class Student:
    """
    Defines a student

    Args:
        first_name
        last_name
        age
    """

    def __init__(self, first_name, last_name, age):
        self.first_name
        self.last_name
        self.age

    def to_json(self):
        return self.__dict__
