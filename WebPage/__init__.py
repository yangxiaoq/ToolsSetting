__version__ = '0.1'
from flask import Flask
from flask import render_template

app = Flask('WebPage')
app.config['SECRET_KEY'] = 'random'
app.debug = True

@app.route('/')
def start():
    return render_template('index.html')