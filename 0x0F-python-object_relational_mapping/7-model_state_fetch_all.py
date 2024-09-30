#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm  import sessionmaker
from model_state import Base,State
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name=sys.argv[3]

    #creating the database engine
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}',pool_pre_ping=True)
    
    # creating a session
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Querying all states and order by stateid
    states = session.query(State).order_by(State.id).all()
    
    # printing the result
    for state in states:
        print(f"{state.id}: {state.name}")

    # Closing the session
    session.close()

