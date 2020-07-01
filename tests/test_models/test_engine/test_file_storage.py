#!/usr/bin/python3
""" File storage test module """

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import json


class Test_File_Storage(unittest.TestCase):
    """ FileStorage test class """

    def test_all(self):
        storage = FileStorage()
        self.assertIsInstance(storage.all(), dict)

    def test_new(self):
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        self.assertTrue(("BaseModel." + obj.id) in storage.all().keys())
        self.assertTrue(obj in storage.all().values())

if __name__ == "__main__":
    unittest.main()
