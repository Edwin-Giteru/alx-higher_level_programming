#!/usr/bin/python3

# a script that print the state object with the name passed as an argument from a database
 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    search_state = sys.argv[4]


    # creating an engine
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}',pool_pre_ping=True)

    # creating a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # query from the database
    state = session.query(State).filter(State.name == search_state).order_by(State.id).first()

    # Displaying the result
    if state:
        print(f"{state.id}")
    else:
        print("Not Found")

    # closing the session
    session.close()

