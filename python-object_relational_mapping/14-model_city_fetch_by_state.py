#!/usr/bin/python3
"""Contains the class definition of a State and
an instance Base = declarative_base().
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State, City).filter(
        City.state_id == State.id).order_by(City.id)

    for state, city in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
