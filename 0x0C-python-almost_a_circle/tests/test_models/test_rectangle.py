#!/usr/bin/python3
""" Defines tests for Rectangle class """


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_init_with_arguments(self):
        rect = Rectangle(4, 5, 1, 2, 10)
        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 2)
        self.assertEqual(rect.id, 10)

    def test_init_without_id(self):
        rect = Rectangle(4, 5, 1, 2)
        self.assertIsNotNone(rect.id)

    def test_area(self):
        rect = Rectangle(4, 5)
        self.assertEqual(rect.area(), 20)

    def test_str_representation(self):
        rect = Rectangle(4, 5, 1, 2, 10)
        self.assertEqual(str(rect), "[Rectangle] (10) 1/2 - 4/5")

    def test_update_with_args(self):
        rect = Rectangle(4, 5, 1, 2, 10)
        rect.update(20, 6, 7, 8, 30)
        self.assertEqual(rect.id, 20)
        self.assertEqual(rect.width, 6)
        self.assertEqual(rect.height, 7)
        self.assertEqual(rect.x, 8)
        self.assertEqual(rect.y, 30)

    def test_update_with_kwargs(self):
        rect = Rectangle(4, 5, 1, 2, 10)
        rect.update(width=6, height=7, x=8, y=30)
        self.assertEqual(rect.width, 6)
        self.assertEqual(rect.height, 7)
        self.assertEqual(rect.x, 8)
        self.assertEqual(rect.y, 30)

    def test_to_dictionary(self):
        rect = Rectangle(4, 5, 1, 2, 10)
        rect_dict = rect.to_dictionary()
        self.assertIsInstance(rect_dict, dict)
        self.assertEqual(rect_dict['id'], 10)
        self.assertEqual(rect_dict['width'], 4)
        self.assertEqual(rect_dict['height'], 5)
        self.assertEqual(rect_dict['x'], 1)
        self.assertEqual(rect_dict['y'], 2)


if __name__ == '__main__':
    unittest.main()

