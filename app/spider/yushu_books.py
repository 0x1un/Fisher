# -*- coding: utf-8 -*-
__author__ = '0x1un'
__date__ = '1/7/19 7:16 PM'

from flask import current_app

from app.libs.httper import HTTP


class YuShuBook:
    # 模型层 MVC M层
    per_page = 15
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.total = 0
        self.books = []

    def __fill_single(self, data):
        """
        如果使用isbn搜索的话, 结果势必只有一条
        :param data:
        :return:
        """
        if data:
            self.total = 1
            self.books.append(data)
            pass

    def __fill_collection(self, data):
        """
        使用关键字搜索, 结果也许有多条或单条或没有
        :param data: api返回的数据
        :return:
        """
        if data:
            self.total = data['total']
            self.books = data['books']
            pass


    def search_by_isbn(self, isbn):
        """ 使用HTTP.get请求搜索isbn
        :param isbn: isbn号
        :return: json of string
        """
        url = self.isbn_url.format(isbn)
        result = HTTP.get(url)
        self.__fill_single(result)

    def search_by_keyword(self, keywords, page=1):
        """ 使用关键字搜索
        :param keywords: 关键字搜索
        :param count: 限制搜索出来的结果数量
        :param start:
        :return: json of string
        """
        # keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'
        url = self.keyword_url.format(keywords, current_app.config['PER_PAGE'],
                                      self.calculate_start(page))

        result = HTTP.get(url)
        self.__fill_collection(result)

    def calculate_start(self, page):
        return (page - 1) * current_app.config['PER_PAGE']
