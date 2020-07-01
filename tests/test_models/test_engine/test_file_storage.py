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
import models


class TestFileStorage(unittest.TestCase):
    """Test class for FileStorage

    Args:
        unittest ([type]): [description]
    """
    def setUp(self):
        """SetUp method"""
        self.bm_instance = BaseModel()
        self.user1 = User()

    def test_base_pep8(self):
        """Test for pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0)

    def test_is_instance(self):
        """Test for instantiation"""
        self.assertIsInstance(models.storage, FileStorage)

    def test_instantiation(self):
        """ tests correct instantiation of FileStorage class  """
        self.assertEqual(type(models.storage).__name__, "FileStorage")

    def test_docstring(self):
        """test docstring in the file"""
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_field_storage_exist(self):
        """ Checks if methods exists """
        self.storage_instance = FileStorage()
        self.assertTrue(hasattr(self.storage_instance, "__init__"))
        self.assertTrue(hasattr(self.storage_instance, "all"))
        self.assertTrue(hasattr(self.storage_instance, "new"))
        self.assertTrue(hasattr(self.storage_instance, "save"))
        self.assertTrue(hasattr(self.storage_instance, "reload"))

    def test_BaseModel_saveStorage(self):
        """ Checks if the save function works """
        self.base1 = BaseModel()
        self.base1.name = "Pinocho"
        self.base1.save()
        models.storage.reload()
        models.storage.all()
        self.assertIsInstance(models.storage.all(), dict)
        self.assertTrue(hasattr(self.base1, 'save'))
        self.assertNotEqual(self.base1.created_at, self.base1.updated_at)

    def test_User_saveStorage(self):
        """ Checks if the save function works """
        self.user1.first_name = "juan"
        self.user1.save()
        models.storage.reload()
        models.storage.all()
        self.assertIsInstance(models.storage.all(), dict)
        self.assertTrue(hasattr(self.user1, 'save'))
        self.assertNotEqual(self.user1.created_at, self.user1.updated_at)

    def test_attributes(self):
        """ tests class attributes"""
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertIsInstance(models.storage._FileStorage__objects, dict)
        self.assertIsInstance(models.storage._FileStorage__file_path, str)

    def test_no_arguments(self):
        """ tests initialization without arguments  """
        with self.assertRaises(TypeError) as error:
            FileStorage.__init__()
            fail = "descriptor '__init__' of 'object' object needs an argument"
            self.assertEqual(str(error.exception), fail)

    def test_arguments(self):
        """ tests __init__ with many arguments"""
        with self.assertRaises(TypeError) as error:
            base = FileStorage(7, 12)
        fail = "object() takes no parameters"
        self.assertEqual(str(error.exception), fail)
