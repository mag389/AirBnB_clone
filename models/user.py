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

    def __init__(self, *args, **kwargs):
        """ Init """
        if len(kwargs) != 0:
            """ Use dictionary to create an instance if given """
            for key, value in kwargs.items():
                if key == '__class__':
                    """ Converts class name string to object type """
                    setattr(self, key, eval(value))
                elif key == 'created_at' or key == 'updated_at':
                    """ Converts datetime string to datetime format """
                    setattr(self, key, dt.strptime(value,
                                                   "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            """ If no dictionary is given, create a new instance with randomly
            generated id and current time """
            self.id = str(uuid.uuid4())
            self.created_at = dt.now()
            self.updated_at = self.created_at
            from models.__init__ import storage
            storage.new(self)