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

devtime = [5]
for i in range(180):
    if i != 0 and i % 5 ==0:
        devtime.append(i+5)

@app.route('/', methods=['GET', 'POST'])
def init():
   return InitData(config.beta)

@app.route('/beta', methods=['GET', 'POST'])
def beta():
   return InitData(config.beta)

@app.route('/pre', methods=['GET', 'POST'])
def pre():
   return InitData(config.pre)

@app.route('/pro', methods=['GET', 'POST'])
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
    return "请求失败" if (shopdata == "请求失败") else render_template("index.html", shoplist=shopdata,devtime = devtime)
