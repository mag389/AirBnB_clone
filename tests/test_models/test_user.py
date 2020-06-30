#!/usr/bin/python3
""" unit testing file for Users """


import unittest
from models.base_model import BaseModel
from models.user import User
import uuid
import json
from datetime import datetime as dt

class TestUser(unittest.TestCase):
    """class for unit testing Users"""

    def test_bm1(self):
        """basic test for attributes """
        u = User()
        self.assertIsInstance(u, BaseModel)
        self.assertIsInstance(u.created_at, dt)
        self.assertIsInstance(u.updated_at, dt)
        self.assertNotIsInstance(u.id, uuid.UUID)
        self.assertIsInstance(u.id, str)

    def test_u1(self):
        """ testing for user specific attributes """
        u = User()
        self.assertIsInstance(u.email, str)
        self.assertIsInstance(u.password, str)
        self.assertIsInstance(u.first_name, str)
        self.assertIsInstance(u.last_name, str)

    def test_u2(self):
        """testing for serialization unsure as of now"""
        u = User()
        
