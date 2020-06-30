#!/usr/bin/python3
""" Unittest for FileStorage class """
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


class TestFileStorage(unittest.TestCase):

    def test_base_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0)

    def test_is_instance(self):
        storage_instance = FileStorage()
        self.assertIsInstance(storage_instance, FileStorage)
