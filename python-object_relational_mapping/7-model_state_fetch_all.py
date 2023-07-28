#!/usr/bin/python3
"""Contains the class definition of a State and
an instance Base = declarative_base().
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State