#!/usr/bin/python3
"""
Defines a function to lookup the
available attributes and methods of an object
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object
    """
    return dir(obj)
