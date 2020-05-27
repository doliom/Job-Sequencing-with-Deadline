from model import InputFormOnline, InputForm
from flask import Flask, render_template, request, redirect, url_for
import os
from algorithms.result import randomFunc, fromFileFunc, onlineFunc

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

from flask_bootstrap import Bootstrap
Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    data = {"bbmSolution": '1, 3, 7, 2, 4, 6, 5',
            "goalBBM": '55',
            "greedySol": '1, 7, 3, 2, 5, 6, 4',
            "goalG": '73'}
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        result = 'ok'
        methodCount = form.countMethod.data
        if form.countMethod.data == 'online':
            return redirect(url_for('online'))
        elif form.countMethod.data == 'fromFile':
            return redirect(url_for('fromFile'))
        else:
             j, w, d , p, randomG, randomB, goalG, goalB = randomFunc()

    else:
        result = None
        methodCount = None
        goalG, goalB, w, d, p, j, randomB, randomG = None, None, None, None, None, None, None, None

    data = {"result": result,
            "methodCount": methodCount,
            "bbmSolution": '1, 3, 7, 2, 4, 6, 5',
            "goalBBM": '55',
            "greedySol": '1, 7, 3, 2, 5, 6, 4',
            "goalGreedy": '73',
            "randomG": randomG,
            "randomB": randomB,
            "w": w,
            "d": d,
            "p": p,
            "j": j,
            "goalG": goalG,
            "goalB": goalB}

    return render_template('index.html',
                           form=form,
                           data=data)

@app.route('/online', methods=['GET', 'POST'])
def online():
    data = None
    result = None
    form = InputFormOnline(request.form)
    if request.method == 'POST' and form.validate():
        result = 'Ok'
        j, w, d, p, solutionG, solutionB, goalG, goalB = onlineFunc(form.d.data, form.w.data, form.p.data)

    else:
        result = None
        goalG, goalB, w, d, p, j, solutionG, solutionB = None, None, None, None, None, None, None, None

    data = {"result": result,
            "solutionG": solutionG,
            "solutionB": solutionB,
            "w": w,
            "d": d,
            "p": p,
            "j": j,
            "goalG": goalG,
            "goalB": goalB}

    return render_template('online.html',
                           form=form, data=data)

# @app.route('/online', methods=['GET', 'POST'])
# def online():
#     if request.method == 'POST':
#         return redirect(url_for('count'))
#     return render_template('online.html')


@app.route('/fromFile', methods=['GET', 'POST'])
def fromFile():
    data = None
    target = os.path.join(APP_ROOT, 'static\csv')
    # print(target)
    filename = None
    result = None
    if not os.path.isdir(target):
        os.mkdir(target)
    if request.method == 'POST':
        result = 'Ok'
        for file in request.files.getlist("file"):
            filename = file.filename
            destination = "/".join([target, filename])
            file.save(destination)
            j, w, d, p, solutionG, solutionB, goalG, goalB = fromFileFunc(destination)

    else:
        result = None
        goalG, goalB, w, d, p, j, solutionG, solutionB = None, None, None, None, None, None, None, None
    data = {"result": result,
            "solutionG": solutionG,
            "solutionB": solutionB,
            "w": w,
            "d": d,
            "p": p,
            "j": j,
            "goalG": goalG,
            "goalB": goalB}

    return render_template("fromfile.html", image_name=filename, data=data)






if __name__ == '__main__':
    app.run(debug=True)
