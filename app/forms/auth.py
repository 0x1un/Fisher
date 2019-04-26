# -*- coding: utf-8 -*-
__author__ = '0x1un'
__date__ = '2/23/19 6:17 PM'
from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length, ValidationError
from app.models.user import User


class BaseForm(Form):
    email = StringField(validators=[DataRequired(), Length(5, 64), Email()])


class RegisterForm(BaseForm):
    password = PasswordField(
        validators=[DataRequired("password can not be blank!"),
                    Length(8, 32)])
    nickname = StringField(
        validators=[DataRequired("nickname can not be blank!"),
                    Length(2, 6)])

    def validate_email(self, field):
        """
        Custom validator for email
        the validator is automatically
        :param field:
        :return:
        """
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already exists!')

    def validate_nickname(self, field):
        """
        Custom validator for nickname
        the validator is automatically
        :param field:
        :return:
        """
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('Nickname is already exists!')


class LoginForm(BaseForm):
    password = PasswordField(
        validators=[DataRequired("password can not be blank!"),
                    Length(8, 32)])


class EmailForm(BaseForm):
    pass
