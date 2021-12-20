#!/usr/bin/python3
"""Lists all `State` objects from `hbtn_0e_6_usa` DB using sqlalchemy.
"""

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from sys import argv

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]
    ))

    Session = sessionmaker(bind=engine)
    session = Session()

    records_list = []

    for instance in session.query(State):
        print("{:d}: {:s}".format(instance.id, instance.name))
