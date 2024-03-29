from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField,
                     RadioField)
from wtforms.validators import InputRequired, Length


class CrawlForm(FlaskForm):
    url = StringField('URL', validators=[InputRequired()])
