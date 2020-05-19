from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

class methodForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    submit = SubmitField("Submit")