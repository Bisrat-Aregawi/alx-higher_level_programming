#!/usr/bin/python3
"""Module deletes records using regex."""

if __name__ == "__main__":
    from sys import argv
    from model_state import State, Base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]
    ))

    session = sessionmaker(bind=engine)()

    del_list = []

    for inst in session.query(State).filter(State.name.like('%a%')):
        del_list.append(inst)

    for rec in del_list:
        session.delete(rec)

    session.flush()
    session.commit()
    session.close()
