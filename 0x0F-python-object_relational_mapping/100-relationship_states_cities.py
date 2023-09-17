#!/usr/bin/python3
"""Defines function to create state with city"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


def create_state_and_city(username, password, database_name):
    """Function to create state and city"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    california = State(name='California')
    california.cities = [City(name='San Francisco')]
    session.add(california)
    session.commit()
    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        pass
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]
        create_state_and_city(username, password, database_name)
