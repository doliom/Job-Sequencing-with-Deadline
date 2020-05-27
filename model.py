from wtforms import Form, FloatField, validators, SelectField, StringField


class InputForm(Form):
    countMethod = SelectField("countMethod",
                              choices=[('online', 'Онлайн'), ('fromFile', 'З файлу'), ('rndm', 'Генерація')])


class InputFormOnline(Form):
    d = StringField(validators=[validators.DataRequired()])
    w = StringField(validators=[validators.DataRequired()])
    p = StringField(validators=[validators.DataRequired()])



