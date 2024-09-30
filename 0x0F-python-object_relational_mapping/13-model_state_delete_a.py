#!/usr/bin/python3
# a script that deletes all States objects with a name containing a letter afrom a database

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    # Capture arguments: MySQL username, password, and database name
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # Create engine and bind session
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}', pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # quering the database
    states_to_remove=session.query(State).filter(State.name.like('%a%')).all()

    # removing matching  states
    for state in states_to_remove:
         # deleting states
         session.delete(state)

         # commiting changes in the database
         session.commit()

    # closing the session
    session.close()

