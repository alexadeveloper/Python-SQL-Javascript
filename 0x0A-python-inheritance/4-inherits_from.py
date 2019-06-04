#!/usr/bin/python3
"""Simple function"""


def inherits_from(obj, a_class):
    """returns if the object is an instance
    that inherited"""
    if issubclass(obj.__class__, a_class):
        if type(obj) != a_class:
            a = True
        else:
            a = False
    else:
        a = False
    return a
