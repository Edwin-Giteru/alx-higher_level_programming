#!/usr/bin/python3
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State, Base

if __name__ == "__main__":
    # Create a connection to the MySQL database
    engine = create_engine(f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all City objects, accessing the related State object, sorted by cities.id
    cities = session.query(City).order_by(City.id).all()

    # Loop through the cities and print the result with the State name
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    session.close()

