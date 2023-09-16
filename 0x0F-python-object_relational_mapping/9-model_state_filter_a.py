#!/usr/bin/python3
"""Defines function to fetch all states"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def filter_states_a(username, password, database_name):
    """Lists all states"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = (session.query(State).filter(State.name.like('%a%'))
                     .order_by(State.id).all())

    if states is None:
        print('Nothing')
    else:
        for state in states:
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
        filter_states_a(username, password, database_name)
