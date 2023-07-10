#!/usr/bin/python3
""" MyList subclass, inherits from list """


class MyList(list):
    """ Fuction to print sorted list
    >>> my_list = MyList()
    >>> my_list.append(1)
    >>> my_list.append(2)
    >>> print(my_list)
    [1, 2]

    """
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
