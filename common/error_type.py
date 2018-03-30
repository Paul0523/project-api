# coding=utf-8

class ErrorType:

    def __init__(self, status, message):
        self.status = status
        self.message = message


NEED_LOGIN = ErrorType(600, '请登录')

DEFAUL_ERROR = ErrorType(500, '服务器开小差了，请稍后再试')

VERIFY_CODE_EXPIRE = ErrorType(10000001, '验证码过期')


VERIFY_CODE_ERROR = ErrorType(100000002, '验证码错误')


