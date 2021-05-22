from WebPage import app
from flask import render_template,request
from WebPage.request.ObtainData import *


@app.route('/beta')
def beta():
    shopdata = betastart()
    return "登录成功" if (shopdata == "success") else render_template("index.html", shoplist=shopdata['data'])

@app.route('/set_eco_shop', methods=['POST'])
def set_eco_shop():
    sel_shop = str(request.form["sel_Shop"])
    SetEcoShop(sel_shop)
