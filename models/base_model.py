#!/usr/bin/python3


"""
BaseModel class that defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime

class BaseModel:
    """
        Summary: Definning the base class
        from which the other classes will inherit
        Attributes:
            id -> Public instance attributes
            created_at -> Public instance attributes
            updated_at -> Public instance attributes
    """
    def __init__(self, *args, **kwargs):
        """
        Initialization of the object/instance attributes
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Writing the __str__ method """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Public instance methods:
            updates the public instance attribute updated_at
            with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Public instance methods
            returns a dictionary containing all keys/values
            of __dict__ of the instance with self.__dict__
            we are making a copy
        """
        dic_BaseClass = self.__dict__
        dic_BaseClass["__class__"] = self.__class__.__name__
        dic_BaseClass["created_at"] = self.created_at.isoformat()
        dic_BaseClass["updated_at"] = self.updated_at.isoformat()
        return dic_BaseClass
