# coding=utf-8
import json

from daylife.dao.sqlengin import AlchemyEncoder


def to_json(obj):
    """
    转换为json输出
    :param obj:
    :return:
    """
    return json.dumps(obj, default=lambda item : item.__dict__, ensure_ascii=False)


def db_to_json(obj):
    """
    把sq
    :param obj:
    :return:
    """
    return json.dumps(obj, cls=AlchemyEncoder, ensure_ascii=False)



def convert_db_to_json_obj(obj):
    """
    把db对象转换为可序列化对象
    :param obj:
    :return:
    """
    return json.loads(db_to_json(obj))