#!/usr/bin/python3
"""Module adds a record into `hbtn_0e_6_usa`'s `states` table"""

if __name__ == "__main__":
    from sys import argv
    from model_state import State, Base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]
    ))

    louisiana = State(name="Louisiana")

    session = sessionmaker(bind=engine)()

    session.add(louisiana)
    session.flush()
    session.commit()

    print(session.query(State).filter_by(name='Louisiana').first().id)
