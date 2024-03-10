#!/usr/bin/python3

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class inherits from BaseModel.

    Public class attributes:
    email: string - empty string
    password: string - empty string
    first_name: string - empty string
    last_name: string - empty string
    """

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of User.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
