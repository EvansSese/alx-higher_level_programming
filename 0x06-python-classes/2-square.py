#!/usr/bin/python3
"""define the square class"""


class Square:
    """this is the square class"""
    def __init__(self, size=0):
        """ This is the init method
        it checks if size is of type int

        Args:
            size: Size of the square

        """
        if (type(size)) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
