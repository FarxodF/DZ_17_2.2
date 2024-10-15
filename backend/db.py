from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String

DATABASE_URL = 'sqlite:///taskmanager.db'
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

from sqlalchemy.schema import CreateTable


def print_sql_queries():
    print(CreateTable(User.__table__).compile(engine))
    print(CreateTable(Task.__table__).compile(engine))


from app.models.__user__ import User
from app.models.__task__ import Task
