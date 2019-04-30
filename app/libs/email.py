from app import mail
from flask_mail import Message
from flask import current_app, render_template, app
from threading import Thread

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
    app = current_app._get_current_object()
    threads = Thread(target=send_async_email, args=[app, msg])
    threads.start()


def send_async_email(app, msg):
    with app.app_context():

        try:
            mail.send(msg)
        except Exception as e:
            pass




