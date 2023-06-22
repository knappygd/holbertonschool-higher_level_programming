#!/usr/bin/python3
"""
Return the dict description for JSON of an object
"""


def class_to_json(obj):
    """
    Return the dict description for JSON of an object
    """
    return obj.__dict__
