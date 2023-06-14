#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    key_list = list(a_dictionary)
    new_dict = {}
    for key in key_list:
        new_dict[key] = (a_dictionary[key] * 2)
    return new_dict
