#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    cont = 0
    for i in list(a_dictionary.keys()):
        if a_dictionary[i] == key:
            a_dictionary[i] = value
            cont += 1
    if cont == 0:
        a_dictionary[key] = value
    return a_dictionary
