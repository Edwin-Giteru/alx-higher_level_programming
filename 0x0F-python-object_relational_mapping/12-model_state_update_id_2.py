#!/usr/bin/python3
# a script that changes the name of a State object from a database

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__=="__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # creating an engine
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}',pool_pre_ping=True)

    # creating a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # fetch the state item with id=2
    state_to_update = session.query(State).filter_by(id=2).first()

    if state_to_update:
        # Changing name of state
        state_to_update.name = "New Mexico"
        
        #Commit the changes to the database
        session.commit()

    # closing the session
    session.close()
