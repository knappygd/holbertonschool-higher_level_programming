#!/usr/bin/python3
"""Contains the class definition of a State and
an instance Base = declarative_base().
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    new = State(name="Louisiana")
    session.add(new)
    session.commit()
    print(new.id)
