#!/usr/bin/python3
"""Contains the class definition of a State and
an instance Base = declarative_base().
"""
from sys import argv
import sqlalchemy
from sqlalchemy import create_engine
from model_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(argv[1], argv[2], argv[3]))

    con = engine.connect()
    states = sqlalchemy.select(State.id, State.name).order_by(State.id)
    res = con.execute(states).fetchall()

    for state in res:
        print("{}: {}".format(state[0], state[1]))
