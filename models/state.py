#!/usr/bin/python3
""" the state calss file """


from models.base_model import BaseModel
import uuid
from datetime import datetime as dt


class State(BaseModel):
    """the state class"""
    name = ""
