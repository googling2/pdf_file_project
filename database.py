import imp
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

username = 'dbmasteruser'
password = 'poiqwq12'
host = 'ls-0f44ac8781fc8ebd52164e957a25ffc2511f62bc.c10g2og22png.ap-northeast-2.rds.amazonaws.com'
port = '3306'  # MySQL 기본 포트
database_name = 'dbmaster'

DB_URL = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database_name}"

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base() 