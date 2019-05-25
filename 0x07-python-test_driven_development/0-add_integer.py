#!/usr/bin/python3
"""Function simple"""


def add_integer(a, b=98):
    """add two integers
    Args:
        a (int): fiist value

    Returns:
        the sum of a and b
    """

    count = 0
    if type(a) is int or type(a) is float:
        count = 1
        if type(a) is float:
            a = int(a)
    else:
        raise TypeError("a must be an integer")
    if type(b) is int or type(b) is float:
        count = 2
        if type(b) is float:
            b = int(b)
    else:
        raise TypeError("b must be an integer")
    if count == 2:
        suma = a + b
    return suma
