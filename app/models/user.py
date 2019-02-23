# -*- coding: utf-8 -*-
from app.models.base import Base
from sqlalchemy import Column, String, Integer, Boolean, Float
from werkzeug.security import generate_password_hash
__author__ = '0x1un'
__date__ = '2/21/19 12:48 PM'


class User(Base):
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    _password = Column('password', String(64))
    email = Column(String(18), unique=True)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)