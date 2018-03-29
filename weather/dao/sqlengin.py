import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from config import config

engine = create_engine(config.get_config('mysql_url'), echo=True)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

def getSession():
    return DBSession()


