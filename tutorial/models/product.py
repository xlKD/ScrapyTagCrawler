from sqlalchemy import Column, Integer, String, Text
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import time

from base import Base

class Product(Base):
    # specify table name
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    price = Column(Integer)
    created_at = Column(Integer, default=int(time.time()))
    modified_at = Column(Integer, default=int(time.time()), onupdate=int(time.time()))

    def __init__( self, name, price ):
        self.name = name
        self.price = price
