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

    def update(self, *args, **kwargs):
        """method update and kargs"""
        argumentos = len(args)
        if argumentos > 0:
            for a in range(argumentos):
                if a == 0:
                    self.id = args[a]
                if a == 1:
                    self.width = args[a]
                    self.height = args[a]
                if a == 2:
                    self.x = args[a]
                if a == 3:
                    self.y = args[a]
        else:
            kargumentos = len(kwargs)
            if kargumentos > 0:
                keys = kwargs.keys()
                for k in keys:
                    if k == 'id':
                        self.id = kwargs[k]
                    if k == 'size':
                        self.width = kwargs[k]
                        self.height = kwargs[k]
                    if k == 'x':
                        self.x = kwargs[k]
                    if k == 'y':
                        self.y = kwargs[k]
