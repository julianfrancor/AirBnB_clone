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
    """Test class for FileStorage

    Args:
        unittest ([type]): [description]
    """
    def setUp(self):
        """SetUp method"""
        self.storage_instance = FileStorage()
        self.__file_path = "file.json"
        self.__objects = {}

    def test_base_pep8(self):
        """Test for pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0)

    def test_is_instance(self):
        """Test for instantiation"""
        self.assertIsInstance(self.storage_instance, FileStorage)

    def test_docstring(self):
        """test docstring in the file"""
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)
