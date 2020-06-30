#!/usr/bin/python3
""" Unittest for BaseModel class """
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


class TestBaseModel(unittest.TestCase):

    def test_base_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/base_model.py'])
        self.assertEqual(result.total_errors, 0)

    def test_is_instance(self):
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)

    def test_attributes(self):
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model.save()
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertEqual(my_new_model.id, my_model.id)
        self.assertEqual(my_new_model.name, my_model.name)
        self.assertEqual(my_new_model.my_number, my_model.my_number)
        self.assertEqual(my_new_model.created_at, my_model.created_at)
        self.assertEqual(my_new_model.updated_at, my_model.updated_at)
        self.assertIsNot(my_model, my_new_model)

    def test_(self):
        my_model = BaseModel()
        my_model.save()
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertEqual(my_new_model.__str__(), "[{}] ({}) {}".format
                         (my_new_model.__class__.__name__,
                          my_new_model.id, my_new_model.__dict__))
