#!/usr/bin/python3
"""Initializing the City class that inherits from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    a class that represents a city name
    Public class attributes:
        state_id: string - empty string: it will be the State.id
        name: string - empty string
    """

    state_id = ""
    name = ""
