#!/usr/bin/python3
# relationship_state.py: Defines the State class with a relationship to City

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    
    # Primary key column
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    
    # State name column
    name = Column(String(128), nullable=False)
    
    # Relationship to the City class, cascade all deletions
    cities = relationship('City', back_populates='state', cascade='all, delete', lazy='joined')

