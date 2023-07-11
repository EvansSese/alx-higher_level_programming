#!/usr/bin/python3
""" Defines a function to write to file """


def write_file(filename="", text=""):
    """ Implements write function """
    with open(filename, 'w', encoding="utf-8") as f:
        bytes_written = f.write(text)
    return bytes_written
