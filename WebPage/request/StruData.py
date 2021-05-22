from WebPage import app
from flask import render_template,request
from WebPage.request.ObtainData import *


@app.route('/set_eco_shop', methods=['POST'])
def set_eco_shop():
    sel_shop = request.form["sel_Shop"]
    invoice = str(request.form["invoice"])
    free_delivery = str(request.form["free_delivery"])
    delivery_markup = str(request.form["delivery_markup"])
    return SetEcoShop(sel_shop,invoice,free_delivery,delivery_markup)

