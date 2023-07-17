#!/usr/bin/python3
"""
Defines the rectangle class
"""


from models.base import Base


class Rectangle(Base):
    """ Implements the rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """ width getter function """
    @property
    def width(self):
        return self.__width

    """ width setter function """
    @width.setter
    def width(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    """ heigth getter function """
    @property
    def height(self):
        return self.__height

    """ height setter function """
    @height.setter
    def height(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    """ x getter function """
    @property
    def x(self):
        return self.__x

    """ x setter function """
    @x.setter
    def x(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    """ y getter function """
    @property
    def y(self):
        return self.__y

    """ y setter function """
    @y.setter
    def y(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    """ area function implementation """
    def area(self):
        return (self.__width * self.__height)

    """ display function implementation """
    def display(self):
        for y in range(self.__y):
            print("")
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end='')
            for j in range(self.__width):
                print("#", end='')
            print("")

    """ String function definition """
    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.__x, self.__y, self.__width, self.__height))

    """ update function implementation """
    def update(self, *args, **kwargs):
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    """ return dictionary function """
    def to_dictionary(self):
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }
