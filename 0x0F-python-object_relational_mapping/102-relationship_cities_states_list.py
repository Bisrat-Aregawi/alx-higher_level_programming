#!/usr/bin/python3
"""Module lists all cities linked to their states."""

if __name__ == "__main__":
    from sys import argv
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_state import Base

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]
    ))

    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)()

    cities_list = session.query(City).all()

    for city in cities_list:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
