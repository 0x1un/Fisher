# -*- coding: utf-8 -*-
from app.libs.helper import is_isbn_or_key
from app.models.base import Base, db
from sqlalchemy import Column, String, Integer, Boolean, Float
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login_manager
from app.models.gift import Gift
from app.models.wish import Wish
from app.spider.yushu_books import YuShuBook
from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from app.libs.enums import PendingStatus
from app.models.drift import Drift
from math import floor
__author__ = '0x1un'
__date__ = '2/21/19 12:48 PM'


class User(Base, UserMixin):
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    _password = Column('password', String(256))
    email = Column(String(18), unique=True)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)

    def generate_token(self, expiration=600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'id': self.id}).decode('utf-8')

    @staticmethod
    def reset_password(new_password, token):
        s = Serializer(secret_key=current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False

        uid = data.get('id')
        with db.auto_commit():
            user = User.query.get_or_404(uid)
            user.password = new_password
        return True

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        """
        @params raw: password
        """
        return check_password_hash(self._password, raw)

    def can_send_drift(self) -> bool:
        """
        determine if there have enough beans to trade
        return: bool
        """
        if self.beans < 1: return False
        success_gifts_count = Gift.query.filter_by(
            uid=self.id, launched=True).count()  # 已经被赠送出去的礼物
        success_receive_count = Drift.query.filter_by(
            requester_id=self.id,
            pending=PendingStatus.Sucess).count()  # 接收到的图书

        return True if floor(success_receive_count / 2) <= floor(
            success_gifts_count) else False  # 保证在索要的同时自己是赠送过礼物的, 防止无限制刷交易虚拟币

    def can_save_to_list(self, isbn):
        if 'isbn' != is_isbn_or_key(isbn):
            return False
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(isbn)
        if not yushu_book.first:
            # 如果此书没有在api数据库中
            return False
        gifting = Gift.query.filter_by(
            uid=self.id, isbn=isbn, launched=False).first()
        wishing = Wish.query.filter_by(
            uid=self.id, isbn=isbn, launched=False).first()
        # 制定规则, 如果心愿单中有与赠送单都没有, 方可上传
        if not gifting and not wishing:
            return True
        return False

    @property 
    def summary(self):
        return dict(
            nickname = self.nickname,
            beans = self.beans,
            email = self.email,
            send_receive = str(self.send_counter) + '/' + str(self.receive_counter)
        )



@login_manager.user_loader
def get_user(uid):
    """
    因为在gift模型中已经关联到了User模型, 此函数与User关联较大, 即从此获取用户id号
    :param uid: 用户id号
    :return: 返回用户模型
    """
    return User.query.get(int(uid))
