class BookViewModel:

    def __init__(self, books):
        self.title = books['title']
        self.publisher = books['publisher']
        self.author = '/'.join(books['author'])
        self.image = books['image']
        self.price = books['price']
        self.summary = books['summary']
        self.pages = books['pages']

    @property
    def intro(self):
        intros = filter(lambda x: True if x else False, [self.author, self.publisher, self.price])
        return ' / '.join(intros)


class BookCollection:

    def __init__(self):
        self.books = []
        self.total = 0
        self.keyword = ''

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
