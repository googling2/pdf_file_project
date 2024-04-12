from email.policy import default
from sqlalchemy import Boolean, Column, Integer, String, Date
from database import Base

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    date = Column(Date)
    complete = Column(Boolean, default=False)

    