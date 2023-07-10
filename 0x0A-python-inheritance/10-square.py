#!/usr/bin/python3
""" Defines a square class """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Implements square class """
    def __init__(self, size):
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2
