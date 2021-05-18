__version__ = '0.1'
from flask import Flask,render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'random'
app.debug = True
from WebPage.request import StruData

@app.route('/')
def start():
   return StruData.betastart()
