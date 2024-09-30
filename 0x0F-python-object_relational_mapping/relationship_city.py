#!/usr/bin/python3
# relationship_city.py: Defines the City class with a foreign key to State

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base  # Import the Base from relationship_state.py

class City(Base):
    __tablename__ = 'cities'
    
    # Primary key column
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    
    # City name column
    name = Column(String(128), nullable=False)
    
    # Foreign key to the state_id in the states table
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    
    # Relationship to the State class
    state = relationship('State', back_populates='cities')

