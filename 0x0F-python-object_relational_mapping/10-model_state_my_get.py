#!/usr/bin/python3
"""Defines function to get a specific state"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def get_state(username, password, database_name, state_name):
    """Lists all states"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_id = session.query(State.id).filter_by(name=state_name)
    if state_id is None:
        print('Not found')
    else:
        print(state_id)
    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        pass
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]
        state_name = sys.argv[4]
        get_state(username, password, database_name, state_name)
