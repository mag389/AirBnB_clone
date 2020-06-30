#!/usr/bin/python3
""" unit testing file for amenities """


import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
import uuid
import json
from datetime import datetime as dt


class TestAmenity(unittest.TestCase):
    """class for unit testing amenities"""

    def test_bm1(self):
        """basic test for attributes """
        u = Amenity()
        self.assertIsInstance(u, BaseModel)
        self.assertIsInstance(u.created_at, dt)
        self.assertIsInstance(u.updated_at, dt)
        self.assertNotIsInstance(u.id, uuid.UUID)
        self.assertIsInstance(u.id, str)

    def test_s1(self):
        """ testing for state specific attributes """
        s = Amenity()
        self.assertIsInstance(s.name, str)

    def test_s2(self):
        """testing for serialization unsure as of now"""
        u = Amenity()
