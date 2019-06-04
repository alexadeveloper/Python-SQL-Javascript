#!/usr/bin/python3
"""A simple function"""
def lookup(obj):
    """ returns the list of available attributes"""
    lista = dir(obj)
    return lista
