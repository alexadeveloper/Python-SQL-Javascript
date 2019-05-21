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

    @property
    def size(self):
        """return the current size"""
        return self.__size

    @size.setter
    def size(self, value):
        """change the value of size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ calculate the area"""

        area = self.__size ** 2
        return area
    
    def my_print(self):
        """print is stdout the suare"""

        for i in range(self.__size):
            if self.__size > 0:
                for j in range(self.__size):
                    print('#', end='')
            print("")
