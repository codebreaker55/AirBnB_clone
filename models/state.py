#!/usr/bin/python3
"""Initializing the State class that inherits from BaseModel"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    a class that represents the name of the state
    Public class attributes:
        name: string - empty string
    """

    name = ""
