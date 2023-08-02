#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine import db_engine
    storage = db_engine.DBStorage()
else:
    from models.engine import file_storage
    storage = file_storage.FileStorage()

storage.reload()
