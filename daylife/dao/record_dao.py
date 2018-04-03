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
    """
    获取用户自己所发的记录
    :param user_id:
    :return:
    """
    session = sqlengin.getSession()
    items = session.execute('select t.*, tt.nickname from user_record t, user_info tt WHERE t.user_id=tt.id AND t.user_id=:user_id ORDER BY t.create_at DESC ', {'user_id': user_id}).fetchall()
    session.close()
    return [ dict(x.items()) for x in items]


def select_follow_by_user_id(user_id):
    """
    获取关注人所发的记录
    :param user_id:
    :return:
    """
    session = sqlengin.getSession()
    items = session.execute('select t.*, ttt.nickname from user_record t, user_follow tt, user_info ttt WHERE t.user_id=ttt.id AND t.user_id=tt.followed_id AND tt.fans_id=:user_id ORDER BY t.create_at DESC', {'user_id': user_id}).fetchall()
    session.close()
    return [dict(x.items()) for x in items]




def select_by_record_id(record_id):
    """
    根据记录Id获取记录
    :param record_id:
    :return:
    """
    session = sqlengin.getSession()
    session.execute('update user_record t set t.hot=t.hot+1 WHERE t.id=:record_id', {'record_id': record_id})
    record = session.execute('select t.*, tt.nickname from user_record t, user_info tt WHERE t.user_id=tt.id AND t.id=:record_id', {'record_id': record_id}).first()
    session.commit()
    session.close()
    return dict(record.items()) if record else None


def select_hot_record():
    """
    获取热门记录
    :return:
    """
    session = sqlengin.getSession()
    items = session.execute('select t.*, tt.nickname from user_record t, user_info tt WHERE t.user_id=tt.id ORDER BY t.hot DESC').fetchall()
    session.close()
    return [dict(x.items()) for x in items]


if __name__ == '__main__':
    print(json_util.to_json(select_by_record_id(2)))