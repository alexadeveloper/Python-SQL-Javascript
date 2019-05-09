#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    num_mayor = 0
    for i in list(a_dictionary.keys()):
        if a_dictionary[i] > num_mayor:
            num_mayor = a_dictionary[i]
            key_mayor = i
    return key_mayor
