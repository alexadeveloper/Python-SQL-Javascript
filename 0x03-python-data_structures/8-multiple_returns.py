#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == '':
        largo = 0
        caracter = None
    else:
        largo = len(sentence)
        caracter = sentence[0]
    return (largo, caracter)
