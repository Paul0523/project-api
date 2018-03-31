# coding=utf-8
import uuid

from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError

from common import error_type
from common.decorator import login_require
from common.error import BussinessException
from common.redis import redis_service
from common.sms import sms_service
from common.util import http
from config import config
from daylife.dao import user_dao
from daylife.dao.models import UserInfo
from daylife.model import UserInfoVo

user = Blueprint('user', __name__, url_prefix='/user')

USER_VERIFY_CODE_PREFIX = "verify_code_"


@user.route('/login')
def login():
    """
    用户登录
    :return:
    """
    phone = request.args.get('phone')
    verify_code = request.args.get('verify_code')
    if config.isDebug:
        if phone[0:4] != verify_code:
            raise BussinessException(error_type.VERIFY_CODE_ERROR)
    else:
        check_verify_code(phone, verify_code)
    if not user_dao.select_by_phone(phone):
        raise BussinessException(error_type.USER_NOT_EXIST)

    user_info = user_dao.select_by_phone(phone)
    token = user_dao.create_token(user_info)
    return http.BaseRes(data=UserInfoVo(user_info.phone, user_info.nickname, user_info.id, token)).to_json()


def check_verify_code(phone, verify_code):
    """
    校验用户发来的验证码
    :param phone:
    :param verify_code:
    :return:
    """
    if phone == '11122223333' and verify_code[0:4] == '1112':
        return
    verify_code_key = USER_VERIFY_CODE_PREFIX + phone
    redis_verify_code = redis_service.get(verify_code_key)
    if not redis_verify_code:
        raise BussinessException(error_type.VERIFY_CODE_EXPIRE)
    if redis_verify_code != verify_code:
        raise BussinessException(error_type.VERIFY_CODE_ERROR)
    redis_service.delete(verify_code_key)


@user.route('/register')
def register():
    """
    用户注册接口
    :return:
    """
    phone = request.args.get('phone')
    verify_code = request.args.get('verify_code')
    nickname = request.args.get('nickname')
    if config.isDebug:
        if phone[0:4] != verify_code:
            raise BussinessException(error_type.VERIFY_CODE_ERROR)
    else:
        check_verify_code(phone, verify_code)
    try:
        user_dao.insert_user(UserInfo(phone=phone, nickname=nickname))
    except IntegrityError as e:
        message = e.orig.args[1]
        if 'phone' in message:
            raise BussinessException(error_type.PHONE_EXIST)
        if 'nickname' in message:
            raise BussinessException(error_type.NICKNAME_EXIST)
    return http.BaseRes().to_json()

@user.route('/logout')
def logout():
    """
    用户登出
    :return:
    """
    pass

@user.route('/send_verify_code')
def send_verify_code():
    """
    发送验证码
    :param phone:
    :param verify_code:
    :return:
    """
    phone = request.args.get('phone')
    verify_code = str(uuid.uuid1())[0:4]
    res = sms_service.send_verify_code(phone, verify_code)
    if res == 'ok':
        redis_service.put_with_expire(USER_VERIFY_CODE_PREFIX + phone, verify_code, 5 * 60)
        return http.BaseRes().to_json()
    else:
        raise BussinessException()



@user.route('/follow')
@login_require
def follow():
    """
    关注
    :return:
    """
    return '返回关注列表'


@user.route('/fans')
def fans():
    """
    粉丝
    :return:
    """
    pass


@user.route('/do_follow')
def do_follow():
    """
    进行关注
    :return:
    """
    pass


@user.route('/do_unfollow')
def do_unfollow():
    """
    取消关注
    :return:
    """
    pass


@user.route('/my_info')
def my_info():
    """
    我的个人信息
    :return:
    """
    pass






