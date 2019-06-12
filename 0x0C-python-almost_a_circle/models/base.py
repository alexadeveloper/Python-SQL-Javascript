#!/usr/bin/python3
"""class Base"""
import json


class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """inicializa Base"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """json from dic"""
        if list_dictionaries is None:
            return "[]"
        if len(list_dictionaries) is 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """json to a file"""
        mylist = []
        if list_objs is None or len(list_objs) is 0:
            mylist = []
        else:
            for i in list_objs:
                mylist.append(i.to_dictionary())
        myjson = Base.to_json_string(mylist)
        with open("{}.json".format(cls.__name__), mode='w', encoding='utf-8')\
                as jsonfile:
            jsonfile.write(myjson)

    def from_json_string(json_string):
        """from string to json"""
        mylist = []
        if json_string is None or json_string is []:
            return mylist
        else:
            return json.loads(json_string)

    def create(cls, **dictionary):
        """create"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
