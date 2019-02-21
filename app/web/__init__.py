# -*- coding: utf-8 -*-
__author__ = '0x1un'
__date__ = '1/8/19 8:45 PM'

from flask import Blueprint

web = Blueprint('web', __name__)

from app.web import book, auth, drift, gift, main, wish

# from app.web import user

