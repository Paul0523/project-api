# coding=utf-8
import datetime
import decimal
import json
import time

from daylife.dao.sqlengin import AlchemyEncoder


class MyJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.datetime,)):
            return int(time.mktime(obj.timetuple()) * 1000)
        elif isinstance(obj, (decimal.Decimal,)):
            return {"val": str(obj), "_spec_type": "decimal"}
        else:
            return super().default(obj)

def to_json(obj):
    """
    转换为json输出
    :param obj:
    :return:
    """
    return json.dumps(obj, cls=MyJSONEncoder, ensure_ascii=False)


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