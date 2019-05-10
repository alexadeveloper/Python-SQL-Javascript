#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    numeros = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    entero = 0
    letra = 'I'
    inversa = roman_string[::-1]
    for i in inversa:
        if numeros[i] >= numeros[letra]:
            letra = i
            entero += numeros[i]
        else:
            entero -= numeros[i]
    return entero
