from .book import BookViewModel
from collections import namedtuple

#  MyGift = namedtuple('MyGift', ['id', 'book', 'wishes_count'])


class MyWishes:

    def __init__(self, gifts_of_mine, wish_count_list):
        self.gifts = []
        self.__gifts_of_mine = gifts_of_mine
        self.__wish_count_list = wish_count_list
        self.gifts = self.__parse()

    def __parse(self,):
        temp_gift = []
        for gift in self.__gifts_of_mine:
            my_gift = self.__matching(gift)
            temp_gift.append(my_gift)
        return temp_gift

    def __matching(self, gift):
        count = 0
        for wish_count in self.__wish_count_list:
            if gift.isbn == wish_count['isbn']:
                count = wish_count['isbn']
        #  my_gift = MyGift(gift.id, BookViewModel(gift.book), count)
        my_gift = {
            'wishes_count': count,
            'book': BookViewModel(gift.book),
            'id': gift.id
        }
        return my_gift
