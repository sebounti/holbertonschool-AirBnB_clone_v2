#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.city import City
import models
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', cascade='all, delete, delete-orphan', backref='state')
    else:
        @property
        def cities(self):
            """
                Getter - returns list of cities instances
                FileStorage relationship between State and City
            """
            listCities = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    listCities.append(city)
            return listCities
