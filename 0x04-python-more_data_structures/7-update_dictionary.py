#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    new_dict = {}
    if key not in a_dictionary:
        a_dictionary[key] = value
    else:
        a_dictionary[key] = value
    return new_dict
