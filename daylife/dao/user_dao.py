# coding=utf-8
import datetime
import uuid

from daylife.dao import sqlengin
from daylife.dao.models import UserInfo, UserToken, UserFollow

"""
session = sqlengin.getSession()
session.close()     
"""

def insert_user(user_info):
    session = sqlengin.getSession()
    session.add(user_info)
    session.commit()
    session.close()

def select_by_phone(phone):
    session = sqlengin.getSession()
    user_info = session.query(UserInfo).filter(UserInfo.phone==phone).first()
    session.close()
    return user_info

def create_token(user_info):
    """
    根据用户信息创建用户token
    :param user_info:
    :return:
    """
    session = sqlengin.getSession()
    session.query(UserToken).filter(UserToken.user_id==user_info.id).filter(UserToken.device_type==0).delete()
    token = str(uuid.uuid1()).replace('-', '')
    expire_at = datetime.datetime.now() + datetime.timedelta(days=90)
    user_token = UserToken(user_id=user_info.id, device_type=0, token=token, expire_at=expire_at)
    session.add(user_token)
    session.commit()
    session.close()
    return token

def select_user_token_info(token):
    session = sqlengin.getSession()
    item = session.query(UserToken).filter(UserToken.token == token).filter(UserToken.device_type == 0).first()
    session.close()
    return item

def add_follow(fans_id, followed_id):
    """
    增加关注
    :param fans_id: 粉丝Id
    :param followed_id: 被关注人Id
    :return:
    """
    user_follow = UserFollow(fans_id=fans_id, followed_id=followed_id)
    session = sqlengin.getSession()
    session.add(user_follow)
    session.commit()
    session.close()

def remove_follow(fans_id, followed_id):
    """
    取消关注
    :param fans_id: 粉丝Id
    :param followed_id:  被关注人Id
    :return:
    """
    session = sqlengin.getSession()
    session.query(UserFollow).filter(UserFollow.followed_id == followed_id).filter(UserFollow.fans_id == fans_id).delete()
    session.commit()
    session.close()


def get_fans(user_id):
    """
    返回用户粉丝列表
    :param user_id:
    :return:
    """
    session = sqlengin.getSession()
    items = session.execute('select tt.* from user_follow t, user_info tt WHERE t.fans_id=tt.id and t.followed_id=:user_id ORDER BY t.create_at DESC', {'user_id': user_id}).fetchall()
    session.close()
    return [dict(x.items()) for x in items]


def get_follows(user_id):
    """
    获取用户关注列表
    :param user_id:
    :return:
    """
    session = sqlengin.getSession()
    items = session.execute('select * from user_follow t, user_info tt WHERE t.followed_id=tt.id AND t.fans_id=:user_id ORDER BY t.create_at DESC', {'user_id', user_id}).fetchall()
    session.close()
    return [dict(x.items()) for x in items]