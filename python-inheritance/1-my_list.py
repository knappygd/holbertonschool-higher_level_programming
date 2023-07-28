#!/usr/bin/python3
"""
Print a sorted list
"""


class MyList(list):
    """
    Prints a list of integers in ascending order
    """
    def print_sorted(self):
        print(sorted(self))
