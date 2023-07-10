#!/usr/bin/python3
""" Defines inherits from function """


def inherits_from(obj, a_class):
    """ Implements the function """
    return issubclass(type(obj), a_class) and type(obj) != a_class
