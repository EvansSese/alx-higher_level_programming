#!/usr/bin/python3
"""Define the square class"""


class Square:
    """define the init method"""
    def __init__(self, size=0):
        """assign the value to the variable


        Args:
            size: Size of the square

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
        if (type(value)) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    """define the area method"""
    def area(self):
        return self.__size ** 2
    """define the print method"""
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size, end='')
                print()
