from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from app.db.db import connect_with_connector

# Create the SQLAlchemy engine using the connection function
engine = connect_with_connector()

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a scoped session for thread safety
SessionScoped = scoped_session(SessionLocal)

def get_db():
    db = SessionScoped()
    try:
        yield db
    finally:
        db.close()
