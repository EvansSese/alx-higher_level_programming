#!/usr/bin/python3
"""Defines function to insert"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def insert_state(username, password, database_name):
    """Inserts state"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    louisiana = State(name='Louisiana')
    session.add(louisiana)
    state_id = session.query(State.id).filter(State.name == 'Louisiana').first()
    print(state_id)
    session.commit()
    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        pass
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]
        insert_state(username, password, database_name)
