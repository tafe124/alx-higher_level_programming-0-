#!/usr/bin/python3
""" Module for testing the Base class """
import unittest
import os
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestBaseMethods(unittest.TestCase):
    """ suite to test Base class """

    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0

    def test_id(self):
        """ Test assigned id """
        b = Base(1)
        self.assertEqual(b.id, 1)

    def test_id_default(self):
        """ Test default id """
        b = Base()
        self.assertEqual(b.id, 1)

    def test_id_nb_objects(self):
        """ Test nb object attribute """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_id_mix(self):
        """ Test nb object attributes and assigned id """
        b1 = Base()
        b2 = Base(8)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 8)
        self.assertEqual(b3.id, 2)

    def test_string_id(self):
        """ Test string id """
        b1 = Base('id 1')
        self.assertEqual(b1.id, 'id 1')

    def test_more_args_id(self):
        """ Test passing more args to init method """
        with self.assertRaises(TypeError):
            new = Base(1, 1)

    def test_access_private_attrs(self):
        """ Test accessing to private attributes """
        b1 = Base()
        with self.assertRaises(AttributeError):
            b1.__nb_objects

    def test_save_to_file(self):
        """ Test JSON file """
        res = "[]"

        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass
        Square.save_to_file(None)
        self.assertTrue(os.path.exists("Square.json"))
        with open("Square.json", "r") as fs:
            self.assertEqual(fs.read(), res)

        Square.save_to_file([])
        with open("Square.json", "r") as fs:
            self.assertEqual(fs.read(), "[]")
