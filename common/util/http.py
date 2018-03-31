from util import json_util


class BaseRes:

    def __init__(self, data=None, status=200, message='OK'):
        self.status = status
        self.message = message
        self.data = data

    def to_json(self):
        """
        返回json串
        :return:
        """
        return json_util.to_json(self.__dict__)