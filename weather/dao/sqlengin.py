import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker


engine = create_engine("mysql+pymysql://root:root@localhost/daylife?charset=utf8mb4", echo=True)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

def getSession():
    return DBSession()


