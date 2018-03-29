# coding=utf-8
from flask import Blueprint

user = Blueprint(name='user', url_prefix='/user')


@user.route('/follow')
def follow():
    """
    关注
    :return:
    """
    pass


@user.route('/fans')
def fans():
    """
    粉丝
    :return:
    """
    pass


@user.route('/do_follow')
def do_follow():
    """
    进行关注
    :return:
    """
    pass


@user.route('/do_unfollow')
def do_unfollow():
    """
    取消关注
    :return:
    """
    pass


@user.route('/my_info')
def my_info():
    """
    我的个人信息
    :return:
    """
    pass






