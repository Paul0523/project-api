# coding=utf-8
import redis

r = redis.Redis(host='127.0.0.1')

def put_with_expire(key, value, expire):
    """
    redis put 操作
    :param key:
    :param value:
    :param expire: 过期时间毫秒
    :return:
    """
    r.set(key, value, expire)


def get(key):
    """
    获取redis值
    :param key:
    :return:
    """
    value = r.get(key)
    if value:
        return value.decode(encoding='utf-8')
    return None

def delete(key):
    """
    删除对应key值
    :param key:
    :return:
    """
    r.delete(key)


if __name__ == '__main__':
    put_with_expire('hello_111', 'llljjlkj', 10)
    # delete('hello_111')
    print(get('hello_111'))