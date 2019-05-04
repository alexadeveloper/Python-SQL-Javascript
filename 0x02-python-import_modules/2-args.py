#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    count = len(argv) - 1
    if count == 0:
        texto = "arguments."
    elif count == 1:
        texto = "argument:"
    else:
        texto = "arguments:"
    print("{} {}".format(count, texto))
    for i in range(len(argv)):
        if i != 0:
            print("{}: {}".format(i, argv[i]))
