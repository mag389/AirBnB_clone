#!/usr/bin/python3
""" the city class file """

from models.base_model import BaseModel
import uuid
from datetime import datetime as dt


class City(BaseModel):
    """ the city class"""
    state_id = ""
    name = ""
