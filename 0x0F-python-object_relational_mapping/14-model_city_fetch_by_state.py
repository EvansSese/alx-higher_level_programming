#!/usr/bin/python3
"""Gets all cities"""


import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def get_all_cities(username, password, database_name):
    """Gets all cities"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = (session.query(City, State)
                   .filter(City.state_id == State.id)
                   .order_by(City.id)
                   .all())
    for city, state in rows:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))


if __name__ == "__main__":
    if len(sys.argv) != 4:
        pass
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]
        get_all_cities(username, password, database_name)
