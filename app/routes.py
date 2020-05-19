from app import app
from flask import render_template, request, url_for, redirect
from werkzeug.utils import secure_filename
from app.forms import methodForm
import os


@app.route('/', methods=['GET', 'POST'])
def index():
    form1 = methodForm()
    return render_template("index.html", form=form1)

