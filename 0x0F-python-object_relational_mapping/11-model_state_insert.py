#!/usr/bin/python3
"""Adds the State object Louisiana to the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":

    usernm = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{:s}:{:s}@localhost/{:s}'
                           .format(usernm, password, dbname))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new = State(name="Louisiana")
    session.add(new)
    session.commit()
    print(new.id)
