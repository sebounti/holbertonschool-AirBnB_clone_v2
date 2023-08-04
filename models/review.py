#!/usr/bin/python3
""" Review module for the HBNB project """
from base_model import BaseModel
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class Review(BaseModel):
    """ Review classto store review information """
    __tablename__ = "Review"
    place_id = Column(String(60), nullable=False)
    user_id = Column(String(60), nullable=False)
    text = Column(String(1024), nullable=False)
    user = relationship("User", backref="reviews")
