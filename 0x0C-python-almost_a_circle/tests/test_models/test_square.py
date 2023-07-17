#!/usr/bin/python3
""" Tests the Square class"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """ Tests square class"""
    def test_init_with_arguments(self):
        square = Square(4, 1, 2, 10)
        self.assertEqual(square.size, 4)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 2)
        self.assertEqual(square.id, 10)

    def test_init_without_id(self):
        square = Square(4, 1, 2)
        self.assertIsNotNone(square.id)

    def test_area(self):
        square = Square(4)
        self.assertEqual(square.area(), 16)

    def test_str_representation(self):
        square = Square(4, 1, 2, 10)
        self.assertEqual(str(square), "[Square] (10) 1/2 - 4")

    def test_update_with_args(self):
        square = Square(4, 1, 2, 10)
        square.update(20, 6, 8, 30)
        self.assertEqual(square.id, 20)
        self.assertEqual(square.size, 6)
        self.assertEqual(square.x, 8)
        self.assertEqual(square.y, 30)

    def test_update_with_kwargs(self):
        square = Square(4, 1, 2, 10)
        square.update(size=6, x=8, y=30)
        self.assertEqual(square.size, 6)
        self.assertEqual(square.x, 8)
        self.assertEqual(square.y, 30)

    def test_to_dictionary(self):
        square = Square(4, 1, 2, 10)
        square_dict = square.to_dictionary()
        self.assertIsInstance(square_dict, dict)
        self.assertEqual(square_dict['id'], 10)
        self.assertEqual(square_dict['size'], 4)
        self.assertEqual(square_dict['x'], 1)
        self.assertEqual(square_dict['y'], 2)


if __name__ == '__main__':
    unittest.main()
