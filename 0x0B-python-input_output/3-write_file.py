#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, encoding='utf-8', mode='w') as archivo:
        escribir = archivo.write(text)
        return escribir
