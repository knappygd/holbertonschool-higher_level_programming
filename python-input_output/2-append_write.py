#!/usr/bin/python3
"""
Append a string at the end
"""


def append_write(filename="", text=""):
    with open(filename, "a") as file:
        file.write(text)
        return len(text)
