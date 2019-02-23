# -*- coding: utf-8 -*-
__author__ = '0x1un'
__date__ = '2/21/19 12:49 PM'

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, SmallInteger

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True # let the Base class not create a data tables.
    status = Column(SmallInteger, default=1)

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

