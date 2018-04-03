# coding: utf-8
from sqlalchemy import Column, DateTime, Index, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class UserFollow(Base):
    __tablename__ = 'user_follow'

    id = Column(Integer, primary_key=True)
    fans_id = Column(Integer, nullable=False)
    followed_id = Column(Integer, nullable=False)
    create_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class UserInfo(Base):
    __tablename__ = 'user_info'

    id = Column(Integer, primary_key=True, nullable=False)
    phone = Column(String(20), nullable=False, unique=True)
    nickname = Column(String(50), primary_key=True, nullable=False, unique=True, server_default=text("''"))
    create_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class UserRecord(Base):
    __tablename__ = 'user_record'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    content = Column(String(500), nullable=False)
    create_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class UserToken(Base):
    __tablename__ = 'user_token'
    __table_args__ = (
        Index('uk_device_type_user_id', 'user_id', 'device_type', unique=True),
    )

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    device_type = Column(Integer, nullable=False, server_default=text("'0'"))
    token = Column(String(50), nullable=False)
    expire_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    create_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
