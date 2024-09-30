# First state model

from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from  sqlalchemy.orm import sessionmaker
import sys

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'

    #Column definition
    id = Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    name = Column(String(128),nullable=False)


if __name__== "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]


    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}',pool_pre_ping=True)

    Base.metadata.create_all(engine)

