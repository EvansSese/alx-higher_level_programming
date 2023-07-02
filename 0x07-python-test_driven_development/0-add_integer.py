#!/usr/bin/python3
""" Function to add 2 integers"""


def add_integer(a, b=98):
    """
    >>> add_integer(1,1)
    2
    >>> add_integer(1.1, 6)
    7
    >>> add_integer(1.1, 1.9)
    2
    >>> add_integer('1', 1)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
    >>> add_integer(1, '1')
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer
    >>> add_integer('1', '1')
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
    >>> add_integer(None, 1)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
    >>> add_integer(1, None)
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer
    >>> add_integer(None, None)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
    >>> add_integer([1,1], 1)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
    >>> add_integer(1, [1,1])
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer
    >>> add_integer([1,1], [1,1])
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
    >>> add_integer((1,1), 1)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
    >>> add_integer(1, (1,1))
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
