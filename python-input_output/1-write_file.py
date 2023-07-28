#!/usr/bin/python3
"""
Reads a file
"""


def write_file(filename="", text=""):
    """
    Writes to a file
    """
    with open(filename, "w") as file:
        file.write(text)
        return len(text)
