from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def func_index():
    return render_template('index.html')


@app.route('/second')
def func_second():
    return render_template('second.html')
