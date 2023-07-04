#!/usr/bin/python3
"""
Defines a locked class
"""


class LockedClass:
    """ Represents the locked class """
    __slots__ = ["first_name"]

    def __setattr__(self, attr, value):
        if attr != "first_name":
            raise AttributeError("'LockedClass' object has no attribute 'last_name'")
        else:
            super().__setattr__(attr, value)
