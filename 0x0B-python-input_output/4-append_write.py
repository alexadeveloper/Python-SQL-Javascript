#!/usr/bin/python3
def append_write(filename="", text=""):
    with open(filename, encoding='utf-8', mode='a') as archivo:
        escribir = archivo.write(text)
        return escribir
