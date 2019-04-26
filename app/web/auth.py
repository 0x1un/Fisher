from app.models.user import User
from app.models.base import db
from . import web
from flask import render_template, request, redirect, url_for, make_response, flash
from app.forms.auth import RegisterForm, LoginForm, EmailForm
from flask_login import login_user, logout_user

__author__ = '0x1un'


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
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('web.login'))
    return render_template('auth/register.html', form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)  # login use and set cookies into the browser
            next: str = request.args.get('next')
            if not next or not next.startswith('/'):
                next: str = url_for('web.index')
            return redirect(next)

        else:
            flash("输入的密码错误或用户名不存在!")
    return render_template('auth/login.html', form=form)


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    form = EmailForm(request.form)
    if request.method == 'POST':
        if form.validate():
            account_email = form.email.data
            user = User.query.filter_by(
                email=account_email).first_or_404()  # 自动处理异常

    return render_template("auth/forget_password_request.html", form=form)


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    pass


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('web.index'))


@web.route('/set/cookie')
def set_cookies():
    response = make_response("Hello, aumujun")
    response.set_cookie('name', 'hello, world', 100)
    return response
