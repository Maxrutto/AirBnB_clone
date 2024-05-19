#!/usr/bin/python3
"""
This file contains a class user that inherits from BaseModel
"""

from models.base_model import BaseModel

class User(BaseModel):
    """
    Represents a user with credentials

    Attributes:
            email (str): The user's email address
            password (str): The user's password
            first_name (str): The user's first name
            last_name (str): The user's last name.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializing a new user instance

        Args:
            *args : variable length argument list.
            **kwargs: arbitrary keywaord arguments for attribute values.
        """
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email', "")
        self.password = kwargs.get('passsword', "")
        self.first_name = kwargs.get('first_name', "")
        self.last_name = kwargs.get('last_name', "")
