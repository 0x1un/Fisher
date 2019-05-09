from . import web
from flask_login import login_required, current_user
from app.models.gift import Gift
from flask import flash, render_template, redirect, url_for
__author__ = '0x1un'


@web.route('/drift/<int:gid>', methods=['GET', 'POST'])
@login_required
def send_drift(gid):
    """
    the users must to be login website.
    """
    current_gift = Gift.query.git_or_404(gid)
    if current_gift.is_myself_books(current_gift.id):
        flash("这本书是你自己的, 不能向自己索要书籍.")
        return redirect(url_for('web.book_detail'), isbn=current_gift.isbn)
    
    can = current_user.can_send_drift()
    if not can:
        return render_template("not_enough_beans.html", beans=current_user.beans)


    gifter = current_user.user.summary
    return render_template("drift.html", gifter=gifter, user_beans=current_user.beans)


    
    


@web.route('/pending')
def pending():
    pass


@web.route('/drift/<int:did>/reject')
def reject_drift(did):
    pass


@web.route('/drift/<int:did>/redraw')
def redraw_drift(did):
    pass


@web.route('/drift/<int:did>/mailed')
def mailed_drift(did):
    pass
