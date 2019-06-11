#!/usr/bin/python3
"""class Base"""


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

    def to_json_string(list_dictionaries):
        """json from dic"""
        if list_dictionaries is None:
            return "[]"
        if len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
