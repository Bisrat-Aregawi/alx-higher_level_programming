#!/usr/bin/python3
"""Module updates `New York` to `New Mexico`."""

if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]
    ))

    sess = sessionmaker(bind=engine)()

    sess.query(State).filter_by(id="2").update({
        "name": "New Mexico"
    })
    sess.flush()
    sess.commit()
    sess.close()
