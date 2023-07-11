#!/usr/bin/python3
""" Loads, add and save """


import json
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    existing_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    existing_list = []
new_args = sys.argv[1:]
updated_list = existing_list + new_args

save_to_json_file(updated_list, "add_item.json")
