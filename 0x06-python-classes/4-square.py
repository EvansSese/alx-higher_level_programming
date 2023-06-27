#!/usr/bin/python3
"""Define square class and find area"""


class Square:
    """define the init method"""
    def __init__(self, size=0):
        """assign the value to the variable


        Args:
            size: The first parameter

        """
        if (type(size)) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    """define the getter"""
    @property
    def size(self):
        return self.__size
    """define the setter"""
    @size.setter
    def size(self, value):
        """this is used to read the size


        Args:
            value: Value to be used
        """
        if (type(value)) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """define the area method"""
    def area(self):
        """find area of circle


        Args:
            size: The size of the square

        Returns:
            int: The area of the square
        """
        return self.__size ** 2
