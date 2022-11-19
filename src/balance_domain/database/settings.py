import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

USERNAME = os.environ["DB_USERNAME"]
HOSTNAME = os.environ["DB_HOSTNAME"]
PASSWORD = os.environ["DB_PASSWORD"]
DATABASE = os.environ["DB_DATABASE"]

SQLALCHEMY_DATABASE_URL = f"mysql://{USERNAME}:{PASSWORD}@{HOSTNAME}/{DATABASE}"

engine = create_engine(SQLALCHEMY_DATABASE_URL,
                       connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def UserAlchemyAdapter():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
