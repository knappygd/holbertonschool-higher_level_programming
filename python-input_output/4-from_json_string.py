#!/usr/bin/python3
"""
Returns an object represented by a string
"""
import json


def to_json_string(my_obj):
    """Returns an object represented by a string"""
    return json.loads(my_obj)
