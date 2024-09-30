#!/usr/bin/python3
# Creating  a State with a City

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # creating an engine and a session
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}',pool_pre_ping=True)

    # creating all tables in the database
    Base.metadata.create_all(engine)

    # creating a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # creating a state with a city
    new_state = State(name="California")
    new_city = City(name="San Francisco",state=new_state)

    # adding the new state and the city to the database
    session.add(new_state)
    session.add(new_city)

    # commiting the changes to the database
    session.commit()

    # closing the session
    session.close()

