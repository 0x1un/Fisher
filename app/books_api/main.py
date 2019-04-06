from flask import Flask
from flask_restful import Resource, Api


from app.books_api.libs.get_json import HTTP

app = Flask(__name__)
api = Api(app)

class GetBook:
    url = 'https://api.douban.com/v2/book/search?q={}&count={}'

    def __init__(self):
        self.title = None
        self.author = None
        self.image = None
        self.price = None
        self.publisher = None
        self.pubdate = None

    def fill(self):
        res = HTTP.get(GetBook.url.format('狂人日记', 1))
        if res:
            books = res['books']
            for book in books:
                self.title = book['title']
                self.author = book['author']
                self.image = book['image']
                self.price = book['price']
                self.publisher = book['price']
                self.pubdate = book['pubdate']





class BooksView(Resource):

    def __init__(self):
        self.g = GetBook()
        self.g.fill()

    def get(self):
        return {
            "title": self.g.title,
            'publisher': self.g.publisher,
            'author': self.g.author,
            'pubdate': self.g.pubdate,
            'image': self.g.image,
            'price': self.g.price

        }
api.add_resource(BooksView, '/')

if __name__ == '__main__':
    app.run(debug=False)
