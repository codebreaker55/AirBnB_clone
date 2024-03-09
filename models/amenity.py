#!/usr/bin/python3
"""Initializing the Amenity class that inherits from BaseModel"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    a class that represents an amenity
    Public class attributes:
        name: string - empty string
    """

    name = ""
