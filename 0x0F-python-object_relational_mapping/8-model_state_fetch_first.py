#!/usr/bin/python3
"""Defines function to fetch all states"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_first_states(username, password, database_name):
    """Lists all states"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).order_by(State.id).first()
    if state is None:
        print('Nothing')
    else:
        print(state.id, end=': ')
        print(state.name)
    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        pass
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]
        list_first_states(username, password, database_name)
