#!/usr/bin/python3
""" Defines from json string function """


import json


def from_json_string(my_str):
    """ Implement json string func """
    json_obj = json.loads(my_str)
    return json_obj
