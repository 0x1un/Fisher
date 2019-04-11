# -*- coding: utf-8 -*-
__author__ = '0x1un'
__date__ = '2/21/19 12:49 PM'

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from sqlalchemy import Column, Integer, SmallInteger
from datetime import datetime
from contextlib import contextmanager


class SQLAlchemy(_SQLAlchemy):

    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e


class Query(BaseQuery):

    def filter_by(self, **kwargs: dict):
        if "status" not in kwargs.keys():
            kwargs['status'] = 1

        return super(Query, self).filter_by(**kwargs)


db = SQLAlchemy(query_class=Query)


class Base(db.Model):
    __abstract__ = True  # let the Base class not create a data tables.
    status = Column(SmallInteger, default=1)
    create_time = Column('create_time', Integer)

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    def set_attrs(self, attrs_dict: dict):
        """

        :param attrs_dict: receiving the forms data, this is a dict, key is forms name, value is forms value
        :return: Nothing returned
        but can be judge the key whether it is models variable,
        if so, set attribute key and value for self
        because the Base class are basic class, Gift class and Book/User class will be inherited Base class.
        id does not want to be assigned
        """
        for k, v in attrs_dict.items():
            if hasattr(self, k) and k != 'id':
                t = hasattr(self, k)
                pass
                setattr(self, k, v)
                # if there is password, then call the User().password, this method used @property,
                # so, it's amazing
                pass

    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        return None
