# coding=utf-8
from common import error_type as et
from util import json_util


def error_handler(exception):
    return exception.to_json()




class BussinessException(Exception):
    """
    业务异常类
    """


    def __init__(self, error_type = et.DEFAUL_ERROR):
        self.status = error_type.status
        self.message = error_type.message


    def to_json(self):
        return json_util.to_json(self)