#!/usr/bin/python3
"""
Returns an object represented by a string
"""
import json


def save_to_json_file(my_obj, filename):
    with open(filename, "w") as file:
        file.write(json.dumps(my_obj))