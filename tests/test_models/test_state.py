#!/usr/bin/python3
""" Unittest for State class """
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


class TestState(unittest.TestCase):

    def test_base_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/state.py'])
        self.assertEqual(result.total_errors, 0)

    def test_is_instance(self):
        model = State()
        self.assertIsInstance(model, State)

    def test_attributes(self):
        my_state = State()
        my_state.name = "Holberton"
        my_state.my_number = 89
        my_state.save()
        my_state_json = my_state.to_dict()
        my_new_state = State(**my_state_json)
        self.assertEqual(my_new_state.id, my_state.id)
        self.assertEqual(my_new_state.name, my_state.name)
        self.assertEqual(my_new_state.my_number, my_state.my_number)
        self.assertEqual(my_new_state.created_at, my_state.created_at)
        self.assertEqual(my_new_state.updated_at, my_state.updated_at)
        self.assertIsNot(my_state, my_new_state)
