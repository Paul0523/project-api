# coding=utf-8

"""
session = sqlengin.getSession()
session.commit()
session.close()
"""
from daylife.dao import sqlengin
from daylife.dao.models import UserRecord


def add_record(user_record):
    session = sqlengin.getSession()
    session.add(user_record)
    session.commit()
    session.close()


def select_by_user_id(user_id):
    session = sqlengin.getSession()
    items = session.query(UserRecord).filter(UserRecord.user_id==user_id).order_by(UserRecord.craete_at.desc()).all()
    session.close()
    return items