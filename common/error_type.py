# coding=utf-8

class ErrorType:

    def __init__(self, status, message):
        self.status = status
        self.message = message


NEED_LOGIN = ErrorType(600, '请登录')

DEFAUL_ERROR = ErrorType(500, '服务器开小差了，请稍后再试')

VERIFY_CODE_EXPIRE = ErrorType(10000001, '验证码过期')


VERIFY_CODE_ERROR = ErrorType(10000002, '验证码错误')

PHONE_EXIST = ErrorType(10000003, '号码已经注册，请直接登录')


NICKNAME_EXIST = ErrorType(10000004, '用户名已经存在')

USER_NOT_EXIST = ErrorType(10000005, '用户不存在，请先注册')

