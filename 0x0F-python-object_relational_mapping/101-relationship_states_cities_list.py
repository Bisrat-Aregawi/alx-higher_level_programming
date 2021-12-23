#!/usr/bin/python3
"""Module lists all states with their corresponding cities."""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]
    ))

    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)()

    states_list = session.query(State).all()

    for state in states_list:
        print("{}: {}".format(
            state.id, state.name
        ))
        for city in state.cities:
            print("    {}: {}".format(
                city.id, city.name
            ))
