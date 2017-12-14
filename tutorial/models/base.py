from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Update this link first
engine = create_engine('mysql+mysqldb://username:password@host:port/db')
Session = sessionmaker(bind=engine)

Base = declarative_base()
