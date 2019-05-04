#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    count = len(argv) - 1
    resultado = 0
    if count > 0:
        for i in range(1, len(argv)):
            resultado += int(argv[i])
    print("{}".format(resultado))
