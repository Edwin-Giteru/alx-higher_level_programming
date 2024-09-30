#!/usr/bin/python3
# a script that prints the first state object ffrom the database

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base,State
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    
    # creating engine
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}',pool_pre_ping=True)

    # creating a session

    Session = sessionmaker(bind=engine)
    session = Session()

    #querying from the database
    first_state = session.query(State).order_by(State.id).first()

    if first_state is None:
        print("Nothing")
    else:
        print(f"{first_state.id}: {first_state.name}")

    # closing the session
    session.close()


