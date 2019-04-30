from app import mail
from flask_mail import Message
from flask import current_app, render_template


def send_mail(to, subject, template, **kwargs):
    """
    here I use the flask-mail plugin, you need install it If you don't have. following
    pip install flask-mail
    """
    msg = Message(
        '[Fisher]' + ' ' + subject,
        sender=current_app.config['MAIL_USERNAME'],
        recipients=[to])
    msg.html = render_template(template, **kwargs)
    mail.send(msg)
