#!/usr/bin/python3
"""Doc Class Square"""


class Square:
    """Square Class"""

    def __init__(self, size=0):
        """Initial size of a square

           Args:
              the size type int
        """
        try:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        except TypeError:
            print("size must be an integer")
