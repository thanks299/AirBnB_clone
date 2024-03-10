#!/usr/bin/python3

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class inherits from BaseModel.

    Public class attributes:
    place_id: string - empty string: it will be the Place.id
    user_id: string - empty string: it will be the User.id
    text: string - empty string
    """

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of Review.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
