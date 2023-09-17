#!/usr/bin/python3
""" Defines the state model """


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_city import City


Base = declarative_base()


class State(Base):
    """ Class that defines state model """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                          cascade='all, delete-orphan')
