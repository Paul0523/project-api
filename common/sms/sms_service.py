# coding=utf-8
import logging
import uuid

from common.sms import demo_sms_send, sms_mapping


def send_verify_code(phone, verify_code):
    """
    发送短信验证码
    :return:
    """
    template_code = getattr(sms_mapping, 'verify_code')['aliyun']['template_code']
    sign_name = getattr(sms_mapping, 'verify_code')['aliyun']['sign_name']
    # {"code": 1234}
    params = "{\"code\": \"" + verify_code + "\"}"
    res = demo_sms_send.send_sms(uuid.uuid1(), phone, sign_name, template_code, params)
    logging.info('发送短信' + str(res))
    if res['Code'] == 'OK':
        return 'ok'
    else:
        return 'fail'


if __name__ == '__main__':
    send_verify_code('15071335527', '1234')