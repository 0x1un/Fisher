# -*- coding: utf-8 -*-
__author__ = '0x1un'
__date__ = '2/21/19 12:58 PM'

from app.models.base import Base
from sqlalchemy import Column, Integer, Boolean, ForeignKey, String
from sqlalchemy.orm import relationship


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User') # 关联User模型
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)