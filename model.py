from wtforms import Form, FloatField, validators, SelectField, StringField


class InputForm(Form):
    countMethod = SelectField("countMethod",
                              choices=[('online', 'Онлайн'), ('fromFile', 'З файлу'), ('rndm', 'Генерація')])

class InputFormOnline(Form):
    d = StringField(label='Директивні строки', validators=[validators.DataRequired()])
    w = StringField(label='Штрафи', validators=[validators.DataRequired()])
    p = StringField(label='Тривалості робіт', validators=[validators.DataRequired()])
