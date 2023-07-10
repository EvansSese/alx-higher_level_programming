#!/usr/bin/python3
""" Defines lookup method """


def lookup(obj):
    """ Implememnt lookup function """
    attributes = []
    methods = []

    for attr in dir(obj):
        if callable(getattr(obj, attr)):
            methods.append(attr)
        else:
            attributes.append(attr)

    return attributes + methods
