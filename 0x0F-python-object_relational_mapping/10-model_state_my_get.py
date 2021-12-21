#!/usr/bin/python3
"""Module fetches passed state name from DB."""

if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]
    ))

    session = sessionmaker(bind=engine)()

    record = []
    for instance in session.query(State).filter(State.name == argv[4]):
        record.append(instance)

    if record:
        print(record[0].id)
    else:
        print("Not found")
