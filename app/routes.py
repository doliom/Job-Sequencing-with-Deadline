from app import app
from flask import render_template, request, url_for, redirect
from werkzeug.utils import secure_filename
from app.forms import InputForm
# from celery_flask import make_celery
#
# celery = make_celery(app)
from app.algorithms.methodtest import *

from flask_bootstrap import Bootstrap

Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        result = compute(form.countMethod)
    else:
        result = None
    print(form, dir(form))
    # def index():
    #     form = InputForm(request.form)
    #     if request.method == 'POST' and form.validate():
    #         result = compute(form.A.data, form.b.data,
    #                          form.w.data, form.T.data)
    #     else:
    #         result = None
    #     print(form, dir(form))
    #     # print form.keys()
    #     for f in form:
    #         print(f.id)
    #         print(f.name)
    #         print(f.label)
    #
    #     return render_template(template_name + '.html',
    #                            form=form, result=result)
    return render_template("index.html", form=form, result=result)


