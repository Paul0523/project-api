class BaseRes:

    def __init__(self, data=None, status=200, message='OK'):
        self.status = status
        self.message = message
        self.data = data