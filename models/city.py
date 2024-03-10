#!/usr/bin/python3
"""
Module for City class
"""
from models.base_model import BaseModel

class City(BaseModel):
    """Custom City class.

    Attributes:
        state_id (str): The ID of the associated State.
        name (str): The name of the City.
    """
    def __init__(self, *args, **kwargs):
        """Initializes a new instance of City.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
