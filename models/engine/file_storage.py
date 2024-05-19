#!/usr/bin/python3
"""
This module contains a class that serializes instance to a JSON file and deserializes JSON file to instances
"""

import json
import os
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """
    This class serializes intance to JSON and deserializes JSON to instance
    """
    __file_path = "file_path"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = f"{type(obj).__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file path __file_path
        """
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w', encoding = "utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file exists; 
        otherwise, do nothing).
        If the file doesn't exist, no exception should be raised
        """
        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, 'r', encoding = "utf-8") as j:
                    obj_dict = json.load(j)
                    self.__object = {}
                    for key, value in obj_dict.items():
                        class_name = value["__class__"]
                        if class_name == "BaseModel":
                            self.__objects[key] = BaseModel(**value)
                        elif class_name == "User":
                            self.__objects[key] = User(**value)
            except FileNotFoundError:
                pass
