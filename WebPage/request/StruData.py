from WebPage import app
from flask import render_template,request
from WebPage.request.ObtainData import *


@app.route('/set_eco_shop', methods=['POST'])
def set_eco_shop():
    sel_shop = str(request.form["sel_Shop"])
    SetEcoShop(sel_shop)

