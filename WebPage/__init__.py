__version__ = '0.1'
from flask import Flask,render_template
from config import config

app = Flask(__name__)
app.config['SECRET_KEY'] = 'random'
app.debug = True
from WebPage.request import StruData

name = ""
passwd = ""
c = ""
baseurl = ""
dataj = {}

@app.route('/')
def start():
   global name, passwd, c, baseurl, dataj
   bc = config.beta
   baseurl = bc['url']
   name = bc['username']
   passwd = bc['passwd']
   c = bc['c']
   dataj = {"name": name, "pwd": passwd, "mcode": c}
   return StruData.betastart()
