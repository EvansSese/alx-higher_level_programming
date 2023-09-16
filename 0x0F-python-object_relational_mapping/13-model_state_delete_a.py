#!/usr/bin/python3
"""Defines function to delete states with a"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def delete_states_a(username, password, database_name):
    """delete states with a"""
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
            session.delete(state)
    session.commit()
    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        pass
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]
        delete_states_a(username, password, database_name)
