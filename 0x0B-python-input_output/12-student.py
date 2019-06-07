#!/usr/bin/python3


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self, attrs=None):
        if isinstance(attrs, list) is False:
            return self.__dict__
        for i in attrs:
            if isinstance(i, str) is False:
                return self.__dict__
        str_dic = {}
        for j in attrs:
            if j in self.__dict__.keys():
                str_dic[j] = self.__dict__[j]
        return str_dic
