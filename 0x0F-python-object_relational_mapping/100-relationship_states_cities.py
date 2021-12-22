#!/usr/bin/python3
"""Module creates State and City with a relationship."""

import sqlalchemy
from sys import argv
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3]
    ))

    Base.metadata.create_all(engine)

    california = State(name="California")
    san_francis = City(name="San Francisco")

    california.cities.append(san_francis)

    session = sessionmaker(bind=engine)()

    session.add(california)
    session.commit()
    session.close()
