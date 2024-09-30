#!/usr/bin/python3
# a script that prints all city objects in a database

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys

if __name__=="__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # creating an engine and session
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}',pool_pre_ping=True)
    
    Base.metadata.create_all(engine)

    Session =sessionmaker(bind=engine)
    session = Session()
    
    # querying the database
    cities = session.query(City,State).join(State).order_by(City.id).all()

    # Printing the results
    for city,state in cities:
        print(f'{state.name}: ({city.id}) {city.name}')

    # closing the session
    session.close()

