#!/usr/bin/python3
def _pow(n):
    return n ** 2


def square_matrix_simple(matrix=[]):
    nueva = []
    for i in matrix:
        nueva.append(list(map(lambda n: _pow(n), i)))
    return nueva
