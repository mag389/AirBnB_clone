#!usr/bin/python3
""" Base Model Module """

import uuid
from datetime import datetime as dt
import json


class BaseModel():
    """ Base Model Class """

    def __init__(self, *args, **kwargs):
        """ Init """
        if len(kwargs) != 0:
            """ Use dictionary to create an instance if given """
            for key, value in kwargs.items():
                if key == '__class__':
                    setattr(self, key, type(self))
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

    def __str__(self):
        """ String representation of the instance """
        return ("[{}] ({}) {}".format(type(self).__name__, self.id,
                                      self.__dict__))

    def save(self):
        """ Saves current datetime to updated_at """
        self.updated_at = dt.now()
        from models.__init__ import storage
        storage.save()

    def to_dict(self):
        """ Returns a dictionary of instance attributes from __dict__ """
        att_dict = {}
        for key, value in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                att_dict[key] = value.isoformat()
            else:
                att_dict[key] = value
        att_dict['__class__'] = type(self).__name__
        return att_dict
