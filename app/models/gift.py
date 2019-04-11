# -*- coding: utf-8 -*-
__author__ = '0x1un'
__date__ = '2/21/19 12:58 PM'

from app.models.base import Base, db
from sqlalchemy import Column, Integer, Boolean, ForeignKey, String, desc, func
from sqlalchemy.orm import relationship
from app.spider.yushu_books import YuShuBook
from flask import current_app


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')  # 关联User模型
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    @classmethod
    def recent(cls):
        # desc 倒序排列

        recent_gift = Gift.query.filter_by(launched=False).group_by(
            Gift.isbn).order_by(desc(Gift.create_time)).limit(
                current_app.config['RECENT_BOOK_COUNT']).distinct().all()

        return recent_gift

    @classmethod
    def get_user_gifts(cls, uid):
        gifts = Gift.query.filter_by(
            uid=uid, launched=False).order_by(desc(Gift.create_time)).all()
        return gifts

    @classmethod
    def get_wish_counts(cls, isbn_list: list):

        from app.models.wish import Wish
        # query in wish table according to the isbn number gift
        count_list = db.session.query(func.count(Wish.id), Wish.isbn).filter(
            # receive the exp
            Wish.launched == False,
            Wish.isbn.in_(isbn_list),
            Wish.status == 1).group_by(Wish.isbn).all()
        count_list = [{'count': w[0], 'isbn': w[1]} for w in count_list]
        return count_list
