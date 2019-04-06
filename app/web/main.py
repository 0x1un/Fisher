from . import web


__author__ = '七月'


@web.route('/')
def index():
    return '<center><h1>哟西</h1></center>'


@web.route('/personal')
def personal_center():
    pass
