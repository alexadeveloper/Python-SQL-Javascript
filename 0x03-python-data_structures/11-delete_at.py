#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    largo = len(my_list)
    if idx < 0 or idx >= largo:
        return my_list
    for i in range(largo):
        if i == idx:
            del my_list[i]
    return my_list
