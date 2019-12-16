#!/usr/bin/python3
"""Prints the State object with the name passed as argument from hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":

    usernm = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    stname = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{:s}:{:s}@localhost/{:s}'
                           .format(usernm, password, dbname))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State)
    stfilter = query.filter(State.name.like(stname)).all()

    if stfilter == []:
        print("Not found")
    else:
        for state in stfilter:
            print("{}".format(state.id))
