from flask import Flask
from weather.service import weather
import socket

app = Flask(__name__)


class PrefixMiddleware(object):
    def __init__(self, app, prefix=''):
        self.app = app
        self.prefix = prefix

    def __call__(self, environ, start_response):
        print(environ['PATH_INFO'])
        if environ['PATH_INFO'].startswith(self.prefix):
            environ['PATH_INFO'] = environ['PATH_INFO'][len(self.prefix):]
            environ['SCRIPT_NAME'] = self.prefix
            return self.app(environ, start_response)
        else:
            start_response('404', [('Content-Type', 'text/plain')])
            return ["This url does not belong to the app.".encode()]

app.wsgi_app = PrefixMiddleware(app.wsgi_app, prefix='/api')

app.register_blueprint(weather)

if __name__ == '__main__':
    hostname = socket.gethostname()
    if (hostname == 'VM-151-99-ubuntu'):
        app.run(port=9999)
    else:
        app.run(debug=True)