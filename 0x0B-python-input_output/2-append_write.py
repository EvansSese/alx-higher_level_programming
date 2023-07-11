#!/usr/bin/python3
""" Function to append text to a file """


def append_write(filename="", text=""):
    """ Implements the append function """
    with open(filename, 'a', encoding="utf-8") as f:
        chars_written = f.write(text)
    return chars_written
