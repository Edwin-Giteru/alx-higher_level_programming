#!/usr/bin/python3
# a script that list all state objects and the corresponding City

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State, Base
import sys

if __name__=="__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # creating an engine and session 
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}',pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # quering the database
    states = session.query(State).outerjoin(City).order_by(State.id,City.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")
    
    session.close()

