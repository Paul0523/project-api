# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class UserInfo(Base):
    __tablename__ = 'user_info'

    id = Column(Integer, primary_key=True, nullable=False)
    nickname = Column(String(50), primary_key=True, nullable=False, server_default=text("''"))


class UserRecord(Base):
    __tablename__ = 'user_record'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    content = Column(String(500), nullable=False)
    craete_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
