#!/usr/bin/python3
"""Module lists all states containing lette `a`."""

if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]
    ))

    session = sessionmaker(bind=engine)()

    for instance in session.query(State).filter(State.name.like('%a%')):
        print("{:d}: {:s}".format(instance.id, instance.name))
