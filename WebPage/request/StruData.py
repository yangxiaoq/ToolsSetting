from WebPage import app
from flask import render_template
from util import Url
from util.HttpRequest import Request
from config import config

req = Request()
name = ""
passwd = ""
c = ""
baseurl = ""
dataj = {}

@app.route('/beta')
def betastart():
    global name,passwd,c,baseurl,dataj
    bc = config.beta
    baseurl = bc['url']
    name = bc['username']
    passwd = bc['passwd']
    c = bc['c']
    req.url = baseurl + Url.check
    dataj = {"name":name,"pwd":passwd,"mcode":"c"}
    req.data = dataj
    resp = req.post()
    print(resp)
    return render_template('index.html')