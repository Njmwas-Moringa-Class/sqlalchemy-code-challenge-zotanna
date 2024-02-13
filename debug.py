#!/usr/bin/env python3
import random
import sys
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import ipdb

# Add the directory containing your models.py to sys.path
sys.path.append('/home/denkim/sqlalchemy-code-challenge-zotanna/lib')

from models import Customer, Restaurant, Review

if __name__ == '__main__':
    # Create engine and session
    engine = create_engine('sqlite:///restaurants.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    fake = Faker()

    # Create database tables
    Base = declarative_base()
    Base.metadata.create_all(engine)

    # Start an ipdb session
    ipdb.set_trace()
