#!/usr/bin/python3
"""review class file for defining reviews of places """
from models.base_model import BaseModel
import uuid
from datetime import datetime as dt


class Review(BaseModel):
    """ review class for reviews of accomadations """
    place_id = ""
    user_id = ""
    text = ""
