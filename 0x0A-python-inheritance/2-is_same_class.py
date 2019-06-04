#!/usr/bin/python3
"""simple function"""


def is_same_class(obj, a_class):
    """ returns True if the object
    is exactly an instance of the specified class"""
    if type(obj) == a_class:
        a = True
    else:
        a = False
    return a
