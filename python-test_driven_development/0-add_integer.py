#!/usr/bin/python3

"""
add_integer - Adds up two integers.
"""


def add_integer(a, b=98):
    """
    Sums up two integers.

    Args:
        a: First number
        b: Second number

    Return:
        The addition of two numbers

    Exception:
        TypeError
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
