#!/usr/bin/python3
"""Function simple"""


def print_square(size):
    """ print a square with the character #
    Args:
    size (int): is the size length of the square
    Return:
    Nothing
    """

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) is not int:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end='')
            print("")
