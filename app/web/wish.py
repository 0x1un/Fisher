from . import web
from flask import render_template
from flask_login import login_required, current_user
from app.models.wish import Wish
from app.models.base import db
from app.view_model.wish import MyWishes
__author__ = '0x1un'


@web.route('/my/wish')
def my_wish():
    uid = current_user.id
    wishes_of_mine = Wish.get_user_wishes(uid)
    gifts_of_mine = [wish.isbn for wish in wishes_of_mine]
    gifts_count_list = Wish.get_gifts_counts(gifts_of_mine)
    view_model = MyWishes(gifts_of_mine, gifts_count_list)
    return render_template('my_wish.html', wishes=view_model.gifts)


@web.route('/wish/book/<isbn>')
def save_to_wish(isbn):
    pass


@web.route('/satisfy/wish/<int:wid>')
def satisfy_wish(wid):
    pass


@web.route('/wish/book/<isbn>/redraw')
def redraw_from_wish(isbn):
    pass
