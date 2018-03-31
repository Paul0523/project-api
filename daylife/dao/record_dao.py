# coding=utf-8

"""
session = sqlengin.getSession()
session.commit()
session.close()
"""
from daylife.dao import sqlengin
from daylife.dao.models import UserRecord, UserInfo
from util import json_util


def add_record(user_record):
    session = sqlengin.getSession()
    session.add(user_record)
    session.commit()
    session.close()


def select_by_user_id(user_id):
    session = sqlengin.getSession()
    items = session.execute('select t.*, tt.nickname from user_record t, user_info tt WHERE t.user_id=tt.id AND t.user_id=:user_id ORDER BY t.create_at DESC ', {'user_id': user_id}).fetchall()
    session.close()
    return [ dict(x.items()) for x in items]

if __name__ == '__main__':
    print(json_util.to_json([ dict(x.items()) for x in select_by_user_id(1)]))