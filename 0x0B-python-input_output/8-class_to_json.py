#!/usr/bin/python3
""" Class to JSON """


import json


def class_to_json(obj):
    """ Class to JSON """
    json_dict = {}
    for attr_name, attr_value in obj.__dict__.items():
        if isinstance(attr_value, (list, dict, str, int, bool)):
            json_dict[attr_name] = attr_value
    return json_dict
