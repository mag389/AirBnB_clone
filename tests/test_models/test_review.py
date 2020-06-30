#!/usr/bin/python3
""" unit testing file for reviews """


import unittest
from models.base_model import BaseModel
from models.review import Review
import uuid
import json
from datetime import datetime as dt


class TestReview(unittest.TestCase):
    """class for unit testing reviewss"""

    def test_bm1(self):
        """basic test for attributes """
        u = Review()
        self.assertIsInstance(u, BaseModel)
        self.assertIsInstance(u.created_at, dt)
        self.assertIsInstance(u.updated_at, dt)
        self.assertNotIsInstance(u.id, uuid.UUID)
        self.assertIsInstance(u.id, str)

    def test_s1(self):
        """ testing for state specific attributes """
        s = Review()
        self.assertIsInstance(s.place_id, str)
        self.assertIsInstance(s.user_id, str)
        self.assertIsInstance(s.text, str)

    def test_s2(self):
        """testing for serialization unsure as of now"""
        u = Review()
