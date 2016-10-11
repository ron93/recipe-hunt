from sqlalchemy import Column, String, ForeignKey, Integer, Float, DateTime, func, SmallInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Recipe(Base):
    __tablename__= "recipe"

    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False)
    ingredients = Column(String,nullable=False)
    steps =Column(String,nullable=False)


    def __init__(self,name):
        self.name=name


    def __repr__(self):
        return "<Dish %r\n" %self.name




# create db
engine = create_engine('sqlite:///app.db')
Base.metadata.create_all(engine)
