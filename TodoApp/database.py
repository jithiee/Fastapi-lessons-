
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABASE_URL = 'sqlite:///./todo.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL , connect_args={"check_same_thread": False})

# check_same_thread: This is specific to SQLite and allows the database connection to be used across multiple 

SessionLocal = sessionmaker( autocommit=False , autoflush=False , bind=engine)
# Summary
# Using sessionmaker ensures:

# Consistent session configuration.
# Easy session management in a scalable way.
# Control over transactions and database operations. This is particularly helpful in multi-threaded or web applications where sessions need to be managed per request.


Base = declarative_base()

# Base = declarative_base() is used in SQLAlchemy to define the base class for all ORM-mapped classes. It is a central part of SQLAlchemy's Object-Relational Mapping (ORM) functionality, which allows you to map Python classes to database tables

