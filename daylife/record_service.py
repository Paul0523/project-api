# coding: utf-8
from flask import Blueprint

from daylife.dao import sqlengin
from daylife.dao.models import UserRecord
from util import json_util

record = Blueprint('record', __name__, url_prefix='/record')

@record.route('/my')
def get_my_record():
    """
    获取个人发布信息
    :return:
    """
    items = sqlengin.getSession().query(UserRecord).all()
    return json_util.db_to_json(items)


@record.route('/my_follow')
def get_my_attention():
    """
    我的关注人发布的记录
    :return:
    """
    pass

@record.route('/publish')
def publish_record():
    """
    发布关注信息
    :return:
    """
    pass





if __name__ == '__main__':
    print(get_my_record())