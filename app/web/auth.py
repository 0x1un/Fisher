from app.models.user import User
from . import web
from flask import render_template, request
from app.forms.auth import RegisterForm
from werkzeug.security import generate_password_hash
__author__ = '七月'


@web.route('/register', methods=['POST', 'GET'])
def register():
    """
    注册试图函数
    :return:
    """
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate():
        # can be render the new page after register successfully
        user = User()
        user.set_attrs(form.data)

    return render_template('auth/register.html', form={'data': {}})


@web.route('/login', methods=['GET', 'POST'])
def login():
    pass


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    pass


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    pass


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    pass
