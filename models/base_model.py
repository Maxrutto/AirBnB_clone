#!/usr/bin/python3
"""
Defines a Basemodel class

"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """ Base class for all other classes """

    def __init__(self, *args, **kwargs):
        """ Initializing object attributes """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at':
                    value = datetime.fromisoformat(value)
                    self.created_at = value
                elif key == 'updated_at':
                    value = datetime.fromisoformat(value)
                    self.updated_at = value
                elif key == 'id':
                    self.id = str(value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """ Prints an official string representation of the class """
        class_name = type(self).__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """ Updates the updated_at with current datetime """
        self.updated_at = datetime.now()
        models.storage.save(self)

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of the instance """
        dict = self.__dict__.copy()
        dict["created_at"] = self.created_at.isoformat()
        dict["update_at"] = self.updated_at.isoformat()
        dict["__class__"] = type(self).__name__

        return dict
