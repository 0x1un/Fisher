# -*- coding: utf-8 -*-
from flask import jsonify, request, render_template, flash
import json
from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_books import YuShuBook
from app.view_model.book import BookViewModel
from app.view_model.book import BookCollection

from . import web

__author__ = '0x1un'
__date__ = '1/8/19 4:49 PM'

# the blueprint will be classification python files


@web.route('/book/search')
def search():
    """
    :param q: 需要搜索的关键字或者isbn号
    :param page: 暂定页数默认为1
    :return: 返回从api中得到的json格式的数据
    """

    form = SearchForm(request.args)
    # 实例化view_model中的批量书籍处理
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        yushu_book = YuShuBook()
        isbn_or_key = is_isbn_or_key(q)

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)
    else:
        # return jsonify(form.errors)
        flash('你输入的关键字不合要求, 请重新输入!')
    # return json.dumps(books, default=lambda o: o.__dict__)
    return render_template('search_result.html', books=books)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    pass


@web.route('/hello')
def hello():
    """ 测试访问
    :return: strings
    """

    return 'hello, flask.'

@web.route('/test2')
def test2():
    r = {
        'name': 'aumujun',
        'age': 19,
    }
    return render_template('test.html', data=r)

@web.route('/test')
def test1():
    from flask import request
    from app.libs.none_local import n
    print(n.v)
    n.v = 2
    print(n.v)
    print('-' * 20)
    print(getattr(request, 'v', None))
    setattr(request, 'v', 2)
    print(request.v)
    return ''
