#!/usr/bin/python3
""" Defines the city model """


from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """ Class that defines city model """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
