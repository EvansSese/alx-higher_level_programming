#!/usr/bin/python3
""" Defines the base geometry class """


class BaseGeometry:
    """ Describes the BaseGeometry
    >>> bg = BaseGeometry()
    >>> bg.integer_validator("name", "John")
    Traceback (most recent call last):
    ...
    TypeError: name must be an integer

    """
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
