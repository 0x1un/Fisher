from wtforms import Form, StringField, IntegerField

from wtforms.validators import Length, NumberRange, DataRequired
from app.models.base import db


class SearchForm(Form):
    q = StringField(validators=[DataRequired(), Length(min=1, max=30)]) # message is error messages
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)