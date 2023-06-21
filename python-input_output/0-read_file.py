#!/usr/bin/python3
"""
Reads a file
"""


def read_file(filename=""):
    """
    Prints the content of a file
    """
    with open(filename, encoding="utf8") as file:
        print(file.read(), end="")
