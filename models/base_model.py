#!/usr/bin/python3
"""Defines the BaseModel class for the HBnB project."""
import models
import uuid
from datetime import datetime


class BaseModel:
    """Common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs representing attributes.
        """
        DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if kwargs:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    self.__dict__[key] = datetime.strptime(value, DATE_FORMAT)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """Returns a human-readable string representation of the BaseModel instance."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """Updates attributes and saves the instance to storage."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the BaseModel instance."""
        result_dict = self.__dict__.copy()
        result_dict['__class__'] = type(self).__name__
        result_dict['created_at'] = self.created_at.isoformat()
        result_dict['updated_at'] = self.updated_at.isoformat()
        return result_dict
