#!/usr/bin/python3
# creating a class city

from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from model_state import Base

class City(Base):
    __tablename__="cities"

    # creating columns of the table
    id = Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    name = Column(String(128),nullable=False)
    state_id = Column(Integer,ForeignKey('states.id'),nullable=False)
