from sqlalchemy import Column, Integer, String, SmallInteger
from app.models.base import base

class Drift(base):
   
    # 接受者的信息
    recipitent_name = Column(String(20), nullable=False)
    address = Column(String(120), nullable=False)
    message = Column(String(50))
    mobile = Column(String(11), nullable=False)
    

    # 书籍的信息
    isbn = Column(String(25), nullable=False)
    book_title = Column(String(100), nullable=False)
    book_author = Column(String(15), nullable=False)
    book_img = Column(String(255), nullable=False)

    # 请求者的信息
    requester_id = Column(Integer(50),nullable=False)
    requester_nickname = Column(String(20), nullable=False)

    # 赠送者的信息
    gifter_id = Column(Integer(50), nullable=False)
    gift_id = Column(Integer(50), nullable=False)
    gifter_nickname = Column(String(20), nullable=False)

    pending = Column('pending', SmallInteger, default=1)


