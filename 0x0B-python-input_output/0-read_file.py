#!/usr/bin/python3
""" define function to read file """


def read_file(filename=""):
    with open(filename, 'r', encoding="utf-8") as f:
        contents = f.read()
