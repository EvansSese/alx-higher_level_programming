#!/usr/bin/python3
""" Defines the state model """


from sqlalchemy import Column, Integer, String
from model_state import Base, State


class City(Base):
    """ Class that defines state model """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey="states.id")
