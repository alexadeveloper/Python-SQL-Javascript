#!/usr/bin/python3
"""Simple function"""


def is_kind_of_class(obj, a_class):
    """returns if the object is an instance"""
    if isinstance(obj, a_class):
        a = True
    else:
        a = False
    return a
