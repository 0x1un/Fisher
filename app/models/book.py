from sqlalchemy import Column, String, Integer

from app.models.base import db


class Book(db.Model):
    book_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), default='佚名')
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)  # unique是否唯一
    summary = Column(String(1000))
    image = Column(String(50))

    def sample(self):
        pass
