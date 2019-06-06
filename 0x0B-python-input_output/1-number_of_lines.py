#!/usr/bin/python3
def number_of_lines(filename=""):
    tlineas = 0
    with open(filename, encoding='utf-8') as archivo:
        for linea in archivo:
            tlineas += 1
        return tlineas
