#!/usr/bin/python3
import json
""" Defines function to convert to json """


def to_json_string(my_obj):
    json_string = json.dumps(my_obj)
    return json_string
