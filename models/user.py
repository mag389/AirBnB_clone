#!/usr/bin/python3
""" User module """

from models.base_model import BaseModel
import uuid
from datetime import datetime as dt


class User(BaseModel):
    """ User class """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
