# coding=utf-8
from functools import wraps

from flask import request

from common import error_type
from common.error import BussinessException
from config import config
from daylife.dao import user_dao


def login_require(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        user_id = request.headers.get('user_id')
        #测试环境不需要token，但是必须要user_id，要不有些用到user_id的地方会出问题
        if not user_id:
            raise  BussinessException(error_type.NEED_LOGIN)

        #正式环境对token进行校验
        # if not config.isDebug:
        token = request.headers.get('token')
        if not user_id or not token:
            raise BussinessException(error_type.NEED_LOGIN)
        user_token = user_dao.select_user_token_info(token)
        #token信息不存在或与存在信息不符合需要进行登录
        if not (user_token and user_token.user_id == int(user_id)):
            raise BussinessException(error_type.NEED_LOGIN)

        return func(*args, **kwargs)
    return decorator