#!/usr/bin/python3
""" Defines function to convert to json """


import json


def to_json_string(my_obj):
    """ Implement json string func """
    json_string = json.dumps(my_obj)
    return json_string
