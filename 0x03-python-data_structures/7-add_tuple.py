#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    largoa = len(tuple_a)
    largob = len(tuple_b)
    if largoa == 0:
        tuple_a = 0, 0
    elif largoa == 1:
        tuple_a = tuple_a[0], 0
    if largob == 0:
        tuple_b = 0, 0
    elif largob == 1:
        tuple_b = tuple_b[0], 0
    resultado = (tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1])
    return resultado
