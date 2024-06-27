#!/usr/bin/python3
"""
Module for Amenity class
"""
from models.base_model import BaseModel

class Amenity(BaseModel):
    """Custom Amenity class.

    Attributes:
        name (str): The name of the Amenity.
    """

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of Amenity.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        super().__init__(*args, **kwargs)
        self.name = ""
