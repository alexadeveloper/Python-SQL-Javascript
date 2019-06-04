#!/usr/bin/python3
"""class simple"""


class BaseGeometry:
    """class with a exception"""
    def area(self):
        """Public instance method"""
        raise Exception("area() is not implemented")
