from app.models.base import db
from app.models.gift import Gift
from . import web
from flask_login import login_required, current_user
from flask import current_app, flash, render_template
from app.view_model.gift import MyGifts
from app.view_model.trade import MyTrades

__author__ = '0x1un'


@web.route('/my/gifts')
@login_required
def my_gifts():

    uid = current_user.id
    gifts_of_mine = Gift.get_user_gifts(uid)
    isbn_list = [gift.isbn for gift in gifts_of_mine]
    wish_count_list = Gift.get_wish_counts(isbn_list)
    view_model = MyTrades(gifts_of_mine, wish_count_list)
    return render_template('my_gifts.html', gifts=view_model.trades)


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    if current_user.can_save_to_list(isbn):
        try:
            gifts = Gift()
            gifts.isbn = isbn
            gifts.uid = current_user.id
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gifts)
            db.session.commit()
        except Exception as e:
            # 如果此时产生了错误, 将回滚到之前
            db.session.rollback()

    else:
        flash('赠送失败, 内部错误')
    pass


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass
