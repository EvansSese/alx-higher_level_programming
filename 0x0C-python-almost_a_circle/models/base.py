#!/usr/bin/python3
"""
This is the base class for the project
"""


import json
import csv
import turtle


class Base:
    """ Defines the base class """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ set up turtle scree """
        window = turtle.Screen()
        window.title("Drawing Rectangles and Squares")
        window.bgcolor("white")

        """Set up the turtle"""
        pen = turtle.Turtle()
        pen.speed(0)
        pen.hideturtle()

        def draw_rectangle(x, y, width, height):
            """function to draw a rectangle"""
            pen.penup()
            pen.goto(x, y)
            pen.pendown()
            pen.begin_fill()
            for _ in range(2):
                pen.forward(width)
                pen.left(90)
                pen.forward(height)
                pen.left(90)
            pen.end_fill()

        def draw_square(x, y, size):
            """function to draw a square"""
            pen.penup()
            pen.goto(x, y)
            pen.pendown()
            pen.begin_fill()
            for _ in range(4):
                pen.forward(size)
                pen.left(90)
            pen.end_fill()
        """Draw rectangles"""
        for rectangle in list_rectangles:
            x, y, width, height = rectangle
            draw_rectangle(x, y, width, height)

        """Draw squares"""
        for square in list_squares:
            x, y, size = square
            draw_square(x, y, size)

        """Close the turtle graphics window on click"""
        window.exitonclick()

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        json_list = []
        if list_objs is not None:
            json_list = [obj.to_dictionary() for obj in list_objs]
        with open(filename, 'w')as f:
            f.write(cls.to_json_string(json_list))

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as f:
                json_data = f.read()
                obj_list = cls.from_json_string(json_data)
                instance_list = [cls.create(**obj) for obj in obj_list]
                return instance_list
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as f:
            wrt = csv.writer(f)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    wrt.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    wrt.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r') as f:
                reader = csv.reader(f)
                instance_list = []
                if cls.__name__ == "Rectangle":
                    for row in reader:
                        id_, width, height, x, y = map(int, row)
                        instance_list.append(cls(id_, width, height, x, y))
                elif cls.__name__ == "Square":
                    for row in reader:
                        id_, size, x, y = map(int, row)
                        instance_list.append(cls(id_, size, x, y))
                return instance_list
        except FileNotFoundError:
            return []
