#!/usr/bin/python3
""" Unittest for User class """
import unittest
import json
import pep8
import os
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from models.engine.file_storage import FileStorage


class TestUser(unittest.TestCase):

    def test_base_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/user.py'])
        self.assertEqual(result.total_errors, 0)

    def test_is_instance(self):
        user1 = User()
        self.assertIsInstance(user1, User)

    def test_attributes(self):
        my_user = User()
        my_user.name = "Holberton"
        my_user.my_number = 89
        my_user.save()
        my_user_json = my_user.to_dict()
        my_new_user = User(**my_user_json)
        self.assertEqual(my_new_user.id, my_user.id)
        self.assertEqual(my_new_user.name, my_user.name)
        self.assertEqual(my_new_user.my_number, my_user.my_number)
        self.assertEqual(my_new_user.created_at, my_user.created_at)
        self.assertEqual(my_new_user.updated_at, my_user.updated_at)
        self.assertIsNot(my_user, my_new_user)
