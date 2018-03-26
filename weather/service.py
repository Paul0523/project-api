from flask import Blueprint, render_template, redirect
from flask import request
import requests
import json
from common import BaseRes

weather = Blueprint('weather', __name__, url_prefix='/weather')

weather_url = 'https://www.sojson.com/open/api/weather/json.shtml?city='


@weather.route('/')
def hello_world():
    city = request.args.get('city')
    if (city == ''):
        return json.dumps(BaseRes(status=404, message='城市不能为空！'), default=lambda obj: obj.__dict__)
    response = requests.get(weather_url + city)
    response = json.loads(response.text)
    if ('status' in response and response['status']== 200):

        data = response['data']

        return json.dumps(BaseRes(data['forecast']), default=lambda obj: obj.__dict__)
    return json.dumps(BaseRes(status=404, message='无该城市数据，请检查参数是否正确！'), default=lambda obj: obj.__dict__)