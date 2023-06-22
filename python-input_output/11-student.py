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
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        attributes = {}
        if not isinstance(attrs, list):
            return self.__dict__
        for attr in attrs:
            if attr in self.__dict__:
                attributes[attr] = self.__dict__[attr]
        return attributes

    def reload_from_json(self, json):
        for k, v in json.items():
            setattr(self, k, v)