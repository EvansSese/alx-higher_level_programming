#!/usr/bin/python3
""" MyList subclass, inherits from list """


class MyList(list):
    """ Fuction to print sorted list """
    def print_sorted(self):
        sorted_list = sorted(self)
        return sorted_list
