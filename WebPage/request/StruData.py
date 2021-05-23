from WebPage import app
import WebPage
from flask import render_template,request
from WebPage.request.ObtainData import *


@app.route('/set_eco_shop', methods=['POST','GET'])
def set_eco_shop():
    if request.method == "POST":
        sel_shop = request.form["sel_Shop"]
        invoice = str(request.form["invoice"])
        free_delivery = str(request.form["free_delivery"])
        delivery_markup = str(request.form["delivery_markup"])
        is_online = request.form["is_online"]
        sel_week = request.form["sel_week"]
        devtime = request.form["devtime"]
        timerule = request.form["timerule"]
        sel_buss = request.form["sel_buss"]
        resultinfo = SetEcoShop(sel_shop,invoice,free_delivery,delivery_markup,is_online,sel_week,devtime,timerule,sel_buss)
        print(resultinfo)
        return resultinfo
    return WebPage.init()

@app.route('/getshopparam', methods=['GET',"POST"])
def getshopparam():
    sid = request.form["sid"]
    return getShopParam(sid)

