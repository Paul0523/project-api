# coding: utf-8
from flask import Blueprint, request

from common.decorator import login_require
from common.util import http
from daylife.dao import sqlengin, record_dao
from daylife.dao.models import UserRecord
from util import json_util

record = Blueprint('record', __name__, url_prefix='/record')

@record.route('/my')
@login_require
def get_my_record():
    """
    获取个人发布信息
    :return:
    """
    user_id = request.headers.get('user_id')
    items = record_dao.select_by_user_id(user_id)
    return http.BaseRes(data=items).to_json()


@record.route('/my_follow')
@login_require
def get_my_follow():
    """
    我的关注人发布的记录
    :return:
    """
    user_id = request.headers.get('user_id')
    items = record_dao.select_follow_by_user_id(user_id)
    return http.BaseRes(data=items).to_json()


@record.route('/hot_record')
@login_require
def get_hot_record():
    """
    获取热门记录
    :return:
    """
    items = record_dao.select_hot_record()
    return http.BaseRes(data=items).to_json()

@record.route('/publish', methods=['post', 'get'])
@login_require
def publish_record():
    """
    发布关注信息
    :return:
    """
    user_id = request.headers.get('user_id')
    content = request.values.get('content')
    user_record = UserRecord(user_id=user_id, content=content)
    record_dao.add_record(user_record)
    return http.BaseRes(message='发布成功！').to_json()


@record.route('/record_detail')
def record_detail():
    """
    记录详细信息
    :return:
    """
    record_id = request.values.get('record_id')
    record = record_dao.select_by_record_id(record_id)
    return http.BaseRes(data=record).to_json()

if __name__ == '__main__':
    print(get_my_record())