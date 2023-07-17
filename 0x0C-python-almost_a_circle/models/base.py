#!/usr/bin/python3
"""
This is the base class for the project
"""


import json


class Base:
    """ Defines the base class """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        json_list =[]
        if list_objs is not None:
            json_list = [obj.to_dictionary() for obj in list_objs]
        with open(filename, 'w')as f:
            f.write(cls.to_json_string(json_list))
