#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.user import User
from models.review import Review
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.base_model import BaseModel
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine import db_engine
    storage = db_engine.DBStorage()
else:
    from models.engine import file_storage
    storage = file_storage.FileStorage()

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review,
           "State": State, "User": User}

storage.reload()
