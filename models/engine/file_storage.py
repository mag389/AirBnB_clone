#!/usr/bin/python3
""" File Storage Module """

import json
from models.base_model import BaseModel

class FileStorage():
    """ File storage class """
    __file_path = "jsonfile.json"
    __objects = {}

    def all(self):
        """ Returns the __objects dictionary """
        return self.__objects

    def new(self, obj):
        """ Adds an object to the __objects dictionary """
        self.__objects[str(type(obj).__name__) + "." + obj.id] = obj

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path) """
        list_of_dicts = []
        for key, value in self.__objects.items():
            list_of_dicts.append(value.to_dict())
        with open(self.__file_path, "w+") as file:
            file.write(json.dumps(list_of_dicts))

    def reload(self):
        """ Deserializes the JSON file to __objects if the file exists """
        with open(self.__file_path, "r") as file:
            list_of_dicts = json.loads(file.read())
        self.__objects = {}
        for obj_dict in list_of_dicts:
            if obj_dict['__class__'] == "BaseModel":
                self.new(BaseModel(**obj_dict))
