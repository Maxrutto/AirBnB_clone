#!/usr/bin/python3
"""
This file contains a basemodel structure that defines
attributes and methods for all other classes that inherit from it

"""

from datetime import datetime
import uuid


class BaseModel:
    """
    Defines the basemodel structure for all other classes
        Attributes:
            id: The unique id for each object
            created_at: The current datetime for each instance
            updated_at: The current datetime each time
            an instance of a each object is created
    """
    def __init__(self, *args, **kwargs):
        """
        To initialize data
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == "created_at" or key == "updated_at":
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        from models import storage
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the object
        """
        obj_dict = {}
        for key, value in self.__dict__.items():
            if not key.startswith('-'):
                obj_dict[key] = value
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """
        Returns a string representation of an object
        """
        class_name = type(self).__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
