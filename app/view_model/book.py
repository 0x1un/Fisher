class BookViewModel:

    def __init__(self, book):
        """
        视图函数, 显示在书籍详情页
        """
        self.title = book['title']
        self.publisher = book['publisher']
        self.author = '/'.join(book['author'])
        self.image = book['image']
        self.price = book['price']
        self.summary = book['summary']
        self.isbn = book['isbn']
        self.pages = book['pages']
        self.pubdate= book['pubdate']
        self.binding = book['binding']

    @property
    def intro(self):
        intros = filter(lambda x: True if x else False, [self.author, self.publisher, self.price])
        return ' / '.join(intros)


class BookCollection:

    def __init__(self):
        self.books = []
        self.total = 0
        self.keyword = ''
    # 填充书籍信息
    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in yushu_book.books]



class _BookViewModel:

    @classmethod
    # handling single book
    # if users search by isb, so the api will be returning one book.
    def package_single(cls, data, keyword):
        returned = {
            'book': [],
            'total': 0,
            'keyword': keyword,
        }
        if data:
            returned['total'] = 1
            returned['books'] = [cls.__cut_book_data(data)]
        return returned

    @classmethod
    # handling more books.
    # if users search by keywords, then api will be returned more books
    def package_collection(cls, data, keyword):
        returned = {'books': [], 'total': 0, 'keyword': keyword}
        if data:
            returned['total'] = data['total']
            # call the method, appending books-data from douban-api
            returned['books'] = [
                cls.__cut_book_data(book) for book in data['books']
            ]
        return returned

    @classmethod
    # return the primary books-data.
    def __cut_book_data(cls, data):
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'pages': data['pages'] or '',
            'price': data['price'],
            'summary': data['summary'] or '',
            'image': data['image'],
            'author': '/'.join(data['author']),
        }
        return book
