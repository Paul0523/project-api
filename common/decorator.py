# coding=utf-8
from functools import wraps

import flask
from flask import request

from common import error_type
from common.error import BussinessException


def login_require(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        user_id = request.args.get('user_id')
        token = request.args.get('token')
        if not user_id or not token:
            raise BussinessException(error_type.NEED_LOGIN)
        return func(*args, **kwargs)
    return decorator