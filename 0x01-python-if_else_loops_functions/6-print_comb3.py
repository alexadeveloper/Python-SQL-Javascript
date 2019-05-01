#!/usr/bin/python3
for m in range(0, 9):
    for n in range(0, 10):
        if m < n:
            if m == 8 and n == 9:
                aux = '\n'
            else:
                aux = ', '
            print("{}{}{}".format(m, n, aux), end='')
