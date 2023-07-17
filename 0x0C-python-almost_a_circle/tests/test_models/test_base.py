#!/usr/bin/python3
""" Tests the base class """


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_init_with_id(self):
        b1 = Base(1)
        self.assertEqual(b1.id, 1)

    def test_init_without_id(self):
        base_obj = Base()
        self.assertIsNotNone(base_obj.id)

    def test_to_json_string_empty_list(self):
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

    def test_to_json_string_with_list(self):
        json_str = Base.to_json_string([{'id': 1, 'name': 'example'},
                                        {'id': 2, 'name': 'test'}])
        self.assertEqual(json_str, '[{"id": 1, "name": "example"}, {"id": 2, "name": "test"}]')

    def test_from_json_string_empty_string(self):
        obj_list = Base.from_json_string("")
        self.assertEqual(obj_list, [])

    def test_from_json_string_with_string(self):
        obj_list = Base.from_json_string(
                '[{"id": 1, "name": "example"},{"id": 2, "name": "test"}]')
        self.assertEqual(len(obj_list), 2)
        self.assertEqual(obj_list[0]['id'], 1)
        self.assertEqual(obj_list[0]['name'], 'example')
        self.assertEqual(obj_list[1]['id'], 2)
        self.assertEqual(obj_list[1]['name'], 'test')


if __name__ == '__main__':
    unittest.main()
