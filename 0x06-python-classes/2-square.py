#!/usr/bin/python3
"""Doc Class Square"""


class Square:
    """Square Class"""

    def __init__(self, size=0):
        """Initial size of a square

           Args:
              the size type int
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
