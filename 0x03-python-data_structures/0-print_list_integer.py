#!/usr/bin/python3
def print_list_integer(my_list=[]):
    largo = len(my_list)
    for i in range(largo):
        print("{:d}".format(my_list[i]))
