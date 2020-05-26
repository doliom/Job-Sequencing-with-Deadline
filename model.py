from wtforms import Form, FloatField, validators, SelectField


class InputForm(Form):

    countMethod = SelectField("countMethod",
                              choices=[('online', 'Онлайн'), ('fromFile', 'З файлу'), ('rndm', 'Генерація')])


