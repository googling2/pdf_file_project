import imp
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

username = 'dbmasteruser'
password = 'poiqwq12'
host = 'localhost'
port = '3306'  # MySQL 기본 포트
database_name = 'dbmaster'

DB_URL = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database_name}"

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base() 