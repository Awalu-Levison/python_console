#!/user/bin/python3
"""module defines class 'FileStorage' <task5>"""

import json
from models.base_mode import BaseModel

class FileStorage:
    """class FileStorage"""
    __file_path = ""
    __objects = {}

    def all(self):
        """returns all objects"""
        return FileStorage.__objects

    def new(self, obj):
        """save obj in __objects"""
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """serialize __objects to JSON file"""
        mydct = {}

        for k, v in FileStorage.__objects.items():
            mydct[k] = v.mydct()

        with open(FileStorage.__file_path, "w") as file:
            json.dump(mydct, file)

    def reload(self):
        """deserializes from __filepath to __objects"""

        mydct = None
        with open(self.__file_path, "r") as file:
            mydct = json.load(file)

        for k, v in mydct.items():
            self.__objects[k] = BaseModel(**v)
