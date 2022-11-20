import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

from balance_domain.tables.tables import create_tables

load_dotenv()

USERNAME = os.environ["DB_USERNAME"]
HOSTNAME = os.environ["DB_HOSTNAME"]
PASSWORD = os.environ["DB_PASSWORD"]
DATABASE = os.environ["DB_DATABASE"]
DIALECT = os.environ["DB_DIALECT"]
PORT = os.environ["DB_PORT"]

SQLALCHEMY_DATABASE_URL = f"{DIALECT}://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)


def get_connection():
    return engine.connect()


def load_tables():
    conn = get_connection()
    create_tables(conn)
