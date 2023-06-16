#!/usr/bin/python3
"""
Print text with a line jump each specific character
"""


def text_indentation(text):
    """
    Print jumpline text
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    s = text[:]

    for char in ".?:":
        list = s.split(char)
        s = ""
        for i in list:
            i = i.strip(" ")
            s = i + char if s is "" else s + "\n\n" + i + char

    print(s[:-3], end="")
