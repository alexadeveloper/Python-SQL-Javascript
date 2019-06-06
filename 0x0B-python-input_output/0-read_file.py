#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, encoding='utf-8') as archivo:
        for linea in archivo:
            print(linea, end='')
