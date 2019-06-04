#!/usr/bin/python3
"""A Class"""


class MyList(list):
    """Class that inherits from list"""

    def print_sorted(self):
        """sorted the list"""
        b = sorted(self)
        print(b)
