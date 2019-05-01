#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        cod = ord(str[i])
        if cod >= 97 and cod <= 122:
            aux = cod - 32
        else:
            aux = cod
        print("{:c}".format(aux), end='')
    print("")
