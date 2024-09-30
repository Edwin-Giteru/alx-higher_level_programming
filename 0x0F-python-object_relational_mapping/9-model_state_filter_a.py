#!/usr/bin/python3
# a script that list all State object that contains the letter a

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # creating an engine
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}',pool_pre_ping=True)

    # creating a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querying from the database
    contains_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id.asc()).all()
    # Display results
    for state in contains_a:
        print(f"{state.id}: {state.name}")

    # closing the session
    session.close()



