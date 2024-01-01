#!/usr/bin/python3
"""
Defining a class filestorage that serializes instances to a JSON
file and deserializes JSON file to instances

"""

import json
from json import loads, dumps
from models.base_model import BaseModel
from os.path import isfile


class FileStorage:
    """ Serializes instances to a JSON file and desrializes JSON files
        to instances

    Attributes:
        __file_path (str): path to json file
        __objects (): Dictionary that stores all objects

    """

    def __init__(self):
        """ Initializing the attributes
        """
        __file_path = "file.json"
        __objects = {}

    def all(self):
        """ Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in the instatiated objects with specific key
        """
        key = f"{obj.__class__.__name__}.{obj.id}"

        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file
            using __file_path
        """
        dict = {
                key: value.to_dict() for key, value
                in FileStorage.__objects.items()}
        json_string = dumps(dict)
        filename = FileStorage.__file_path
        with open(filename, "w") as f:
            f.write(json_string)

    def reload(self):
        """ Deserializes the JSON file to __objects
        """
        allowed_classes = ["BaseModel"]
        filename = FileStorage.__filepath
        if isfile(filename):
            with open(filename, "r") as f:
                json_string = f.read(filename)
                json_load = loads(json_string)
            for key, value in json_load.items():
                class_name, obj_id = key.split(".")
            if class_name in allowed_classes:
                eval("self.new({}(**value))".format(class_name))
