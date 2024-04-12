from email.policy import default
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship
from database import Base

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    date = Column(Date)
    complete = Column(Boolean, default=False)
    files = relationship("UploadedFile", back_populates="todo") # type: ignore

class UploadedFile(Base):
    __tablename__ = "uploaded_files"
    id = Column(Integer, primary_key=True)
    todo_id = Column(Integer, ForeignKey('todos.id'), nullable=False)
    filename = Column(String(255), nullable=False)
    uploaddate = Column(DateTime, nullable=False)
    todo = relationship("Todo", back_populates="files") # type: ignore