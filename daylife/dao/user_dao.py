# coding=utf-8
import datetime
import uuid

from daylife.dao import sqlengin
from daylife.dao.models import UserInfo, UserToken

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


if __name__ == '__main__':
    print(select_user_token_info('89bb221c349511e89cecb8e85634f0ac'))