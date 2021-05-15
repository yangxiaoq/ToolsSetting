__version__ = '0.1'
from flask import Flask,url_for

app = Flask('WebPage')
app.config['SECRET_KEY'] = 'random'
app.debug = True

@app.route("/")
def start():
    return url_for("beta")
