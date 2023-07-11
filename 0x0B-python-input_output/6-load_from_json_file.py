#!/usr/bin/python3
""" Loads from JSON file """


import json


def load_from_json_file(filename):
    """ function to load from file """
    with open(filename, 'r', encoding="utf-8") as f:
        json_obj = json.load(f)
    return json_obj
