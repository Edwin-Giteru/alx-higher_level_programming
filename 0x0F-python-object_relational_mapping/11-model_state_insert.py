#!/usr/bin/python3
# a script that adds a state to the database

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__=="__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    #Creating an engine
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}',pool_pre_ping=True)

    # creating a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # adding a new state object with the name 'Louisiana'
    new_state =State(name="Louisiana")

    # Add new state to the session
    session.add(new_state)
    
    # commitiing the session to add a new instance in the database
    session.commit()

    # printing the id of the newly created state
    print(new_state.id)

    # close the session

    session.close()

