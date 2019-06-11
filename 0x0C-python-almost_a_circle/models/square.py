#!/usr/bin/python3
"""class square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """instantiation of Square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format
                (self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """initialize size"""
        return self.width

    @size.setter
    def size(self, value):
        """update size"""
        self.width = value
        self.height = value
