from sqlalchemy.schema import CreateTable
from app.backend.db import Base, engine
from app.models.__user__ import User
from app.models.__task__ import Task


Base.metadata.create_all(bind=engine)  # Печать SQL-запросов для создания таблиц
print(CreateTable(User.__table__).compile(engine))
print(CreateTable(Task.__table__).compile(engine))

