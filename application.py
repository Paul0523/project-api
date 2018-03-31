import sys

import io
from flask import Flask

from common.error import error_handler, BussinessException
from common.middleware import PrefixMiddleware
from config import config
from daylife.record_service import record
from daylife.user_service import user
import logging

logging.basicConfig(level=logging.DEBUG)
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
app = Flask(__name__)
app.wsgi_app = PrefixMiddleware(app.wsgi_app, prefix='/api')
# app.register_blueprint(weather)
app.register_blueprint(record)
app.register_blueprint(user)
app.register_error_handler(BussinessException, error_handler)

if __name__ == '__main__':
    if (not config.isDebug):
        app.run(port=9999)
    else:
        app.run(debug=True)
