# -*- coding: utf-8 -*-
__version__ = '0.1'
from flask import Flask,render_template
from config import config
from util.Util import *

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
def init():
   return InitData(config.beta)

@app.route('/beta')
def beta():
   return InitData(config.beta)

@app.route('/pre')
def pre():
   return InitData(config.pre)

@app.route('/pro')
def pro():
   return InitData(config.pro)

def InitData(cifdata):
    type = 1
    global name, passwd, c, baseurl, dataj
    bc = cifdata
    c = bc['c']
    rc = readc()
    if (rc != "" and rc != bc['c']) or rc == "":
        type = 2
        writec(c)
    baseurl = bc['url']
    name = bc['username']
    passwd = bc['passwd']
    dataj = {"name": name, "pwd": passwd, "mcode": c}
    shopdata = StruData.start() if (type == 1) else StruData.check()
    return "请求失败" if (shopdata == "请求失败") else render_template("index.html", shoplist=shopdata)
