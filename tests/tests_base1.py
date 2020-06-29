#!/usr/bin/python3
""" first unit testing file for basemodel """


import unittest
from models.base_model import BaseModel
import uuid
import json
from datetime import datetime as dt


class TestBase(unittest.TestCase):
    """unit testing class"""

    def test_bm1(self):
        """basic test for some attributes """
        b = BaseModel()
        self.assertIsInstance(b, BaseModel)
        self.assertIsInstance(b.created_at, dt)
        self.assertIsInstance(b.updated_at, dt)
        self.assertNotIsInstance(b.id, uuid.UUID)
        self.assertIsInstance(b.id, str)
