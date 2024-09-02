#!/user/bin/python3
"""Base class to hold the projects models"""

from uuid import uuid4
from datetime import datetime
from copy import deepcopy
import json


class BaseModel:
    """Base Class model"""

    format = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *_, **kwargs):
        """constructor"""
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k != "__class__":
                    if k == "created_at" or k == "updated_at":
                        setattr(self, k, datetime.strptime(v, BaseModel.format))
                    else:
                        setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = deepcopy(self.created_at)

    def save(self):
        """public instance methods: save object"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns object representation"""
        mydct = {}

        mydct.update(self.__dict__)
        mydct["__class__"] = self.__class__.__name__
        mydct["created_at"] = self.created_at.strftime(BaseModel.format)
        mydct["updated_at"] = self.updated_at.strftime(BaseModel.format)
        return mydct

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
