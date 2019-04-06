# -*- coding: utf-8 -*-
from flask import Flask
from app.models.book import db
from flask_login import LoginManager

__author__ = '0x1un'
__date__ = '1/8/19 8:43 PM'

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)
    db.init_app(app)
    db.create_all(app=app)
    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册账号'
    return app


def register_blueprint(app):
    """ 注册蓝图

    :param app: 传入app, 使用app注册蓝图
    :return:
    """
    from app.web.book import web
    app.register_blueprint(web)
