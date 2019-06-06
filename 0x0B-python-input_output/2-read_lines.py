#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    tlineas = 0
    with open(filename, encoding='utf-8') as archivo:
        for linea in archivo:
            tlineas += 1
            if nb_lines <= 0 or nb_lines >= tlineas:
                print(linea, end='')
