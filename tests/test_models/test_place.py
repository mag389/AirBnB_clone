#!/usr/bin/python3
""" unit testing file for places """


import unittest
from models.base_model import BaseModel
from models.place import Place
import uuid
import json
from datetime import datetime as dt


class TestPlace(unittest.TestCase):
    """class for unit testing Places"""

    def test_bm1(self):
        """basic test for attributes """
        u = Place()
        self.assertIsInstance(u, BaseModel)
        self.assertIsInstance(u.created_at, dt)
        self.assertIsInstance(u.updated_at, dt)
        self.assertNotIsInstance(u.id, uuid.UUID)
        self.assertIsInstance(u.id, str)

    def test_s1(self):
        """ testing for state specific attributes """
        s = Place()
        self.assertIsInstance(s.name, str)
        self.assertIsInstance(s.city_id, str)
        self.assertIsInstance(s.user_id, str)
        self.assertIsInstance(s.description, str)
        self.assertIsInstance(s.number_rooms, int)
        self.assertIsInstance(s.number_bathrooms, int)
        self.assertIsInstance(s.max_guest, int)
        self.assertIsInstance(s.price_by_night, int)
        self.assertIsInstance(s.latitude, float)
        self.assertIsInstance(s.longitude, float)
        self.assertIsInstance(s.amenity_ids, list)

    def test_s2(self):
        """testing for serialization unsure as of now"""
        u = Place()
