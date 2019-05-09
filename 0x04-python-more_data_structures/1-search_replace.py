#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nueva = []
    for i in range(len(my_list)):
        nueva.append(replace if my_list[i] == search else my_list[i])        
    return nueva
