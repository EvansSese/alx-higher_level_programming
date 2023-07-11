#!/usr/bin/python3
""" Class Student """


class Student:
    """ Student class """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            attrs = self.__dict__.keys()
        else:
            attrs = filter(lambda attr: attr in self.__dict__, attrs)
        json_dict = {}
        for attr_name in attrs:
            attr_value = getattr(self, attr_name)
            if isinstance(attr_value, (list, dict, str, int, bool)):
                json_dict[attr_name] = attr_value
        return json_dict

    def reload_from_json(self, json):
        for attr_name, attr_value in json.items():
            setattr(self, attr_name, attr_value)
