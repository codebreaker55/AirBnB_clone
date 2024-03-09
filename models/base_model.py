#!/usr/bin/python3
"""initializing BaseModel class"""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Representing the BaseModel class"""

    def __init__(self, *args, **kwargs):
        """
        Public instance attributes:
            id: string - assign with an uuid when an instance is created
            created_at: datetime - assign with the current datetime,
            when an instance is created.
            updated_at: datetime - assign with the current datetime,
            when an instance is created.
            and it will be updated every time the object is changed.
        Args:
            *args (any): not used
            **kwargs (dict): Key and value pair of attributes
        """

        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self):
        """
        returns the print/str representation of the BaseModel instance
        should print: [<class name>] (<self.id>) <self.__dict__>
        """

        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)

    def save(self):
        """
        updates public instance attribute updated_at with the current datetime
        """

        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values,
        of __dict__ of the instance:by using self.__dict__,
        only instance attributes set will be returned
        a key __class__ will  be added to this dictionary
        with the class name of the object
        """

        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict
