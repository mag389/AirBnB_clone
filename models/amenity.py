#!/usr/bin/python3
"""amenity class file """


from models.base_model import BaseModel
import uuid
from datetime import datetime as dt


class Amenity(BaseModel):
    """ amenity class"""
    name = ""
