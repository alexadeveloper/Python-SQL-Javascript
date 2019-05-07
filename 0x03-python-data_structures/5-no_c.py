#!/usr/bin/python3
def no_c(my_string):
    a = [x for x in my_string if x not in 'cC']
    a = ''.join(a)
    return a
