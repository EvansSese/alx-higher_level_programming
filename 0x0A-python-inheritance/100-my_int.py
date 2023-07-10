#!/usr/bin/python3
""" Defines MyInt """


class MyInt(int):
    """ Implement ovverides """
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
