from WebPage import app
from flask import render_template
from util import Url
from util.HttpRequest import Request
from config import config
import WebPage as wp

req = Request()

@app.route('/beta')
def betastart():
    req.url = wp.baseurl + Url.check
    req.data = wp.dataj
    loginresp = req.post()
    if loginresp == "success":
        refresh()
    return "登录成功" if (loginresp == "success") else render_template("index.html")

def refresh():
    req.url = wp.baseurl + "/c/" + wp.c
    req.data = None
    refeshresp = req.get()
    if refeshresp == "success":
        getBrandList()

def getBrandList():
    req.url = wp.baseurl + Url.getBrandList +"?mcode=" + wp.c
    req.data = wp.dataj
    branresp = req.get()
