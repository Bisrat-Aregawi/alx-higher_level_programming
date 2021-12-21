#!/usr/bin/python3
"""Module fetches all cities by their states."""

if __name__ == "__main__":
    from model_state import State, Base
    from model_city import City
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]
    ))

    sess = sessionmaker(bind=engine)()

    for c, s in sess.query(City, State).filter(City.state_id == State.id):
        print("{}: ({}) {}".format(s.name, c.id, c.name))
