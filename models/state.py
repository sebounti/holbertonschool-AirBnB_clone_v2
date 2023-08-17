#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
import models
from models import storage
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='delete')

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        @property
        def cities(self):
            """
                Getter - returns list of cities instances
                FileStorage relationship between State and City
            """
            listCities = []

            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    listCities.append(city)
            return listCities
