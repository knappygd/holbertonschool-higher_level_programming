#!/usr/bin/python3
"""
Returns an object represented by a string
"""
import json


def from_json_string(my_str):
    """Returns an object represented by a string"""
    return json.loads(my_str)
