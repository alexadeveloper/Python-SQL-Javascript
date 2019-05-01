#!/usr/bin/python3
for i in range(0, 100):
    if i < 10:
        aux = 0
    else:
        aux = ''
    if i < 99:
        esp = ', '
    else:
        esp = '\n'
    print("{}{}{}".format(aux, i, esp), end='')
