#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        resultado = fct(*args)
    except Exception as error:
        print("Exception: {}".format(error), file=sys.stderr)
        resultado = None
    return resultado
