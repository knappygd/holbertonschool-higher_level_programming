#!/usr/bin/python3
"""
Append a string at the end
"""


def append_write(filename="", text=""):
    """
    Append text at the end of a file
    """
    with open(filename, "a") as file:
        file.write(text)
        return len(text)
