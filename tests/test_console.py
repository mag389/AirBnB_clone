#!/usr/bin/python3
""" unit testing file for Users """


import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from console import HBNBCommand
from models.user import User
import uuid
import json
from datetime import datetime as dt
from unittest.mock import patch
import io


class TestConsole(unittest.TestCase):
    """class for unit testing Users"""

    def test_bm1(self):
        """basic test for attributes """
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help show")
            comp = "prints string representation of object based on ID"
            self.assertEqual(f.getvalue().strip(), comp)

    def test_u1(self):
        """ testing for user specific attributes """
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help all")
            comp = "Prints all object of certain type, or all objects"
            self.assertEqual(f.getvalue().strip(), comp)

    def test_u2(self):
        """testing for serialization unsure as of now"""
        u = User()
