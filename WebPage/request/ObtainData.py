from util.HttpRequest import Request
from config import config
import WebPage as wp
from util import Url

req = Request()
sbid,said = "",""
shoplist = []

def start():
    reinfo = refresh()
    if reinfo == "check":
        checkdata = check()
        return checkdata
    else:
        return reinfo


def check():
    req.url = wp.baseurl + Url.check
    req.data = wp.dataj
    loginresp = req.post()
    if loginresp == "success":
        shopdata = refresh()
    else:
        shopdata = "请求失败"
    return shopdata


def refresh():
    req.url = wp.baseurl + "/c/" + wp.c
    req.data = None
    refeshresp = req.get()
    if refeshresp == "success":
        return getBrandList()
    else:
        return "check"

def getBrandList():
    req.url = wp.baseurl + Url.getBrandList +"?mcode=" + wp.c
    req.data = wp.dataj
    branresp = req.get()
    return getFRegionList(branresp['data'][0]['id'])

def getFRegionList(bid):
    req.url = wp.baseurl + Url.getFRegionList + "?mcode=" + wp.c + "&bid = " + bid
    FRegionresp = req.get()
    return getShopListAll(bid,FRegionresp['data'][0]['aid'])

def getShopListAll(bid,aid):
    global sbid,said
    sbid = bid
    said = aid
    req.url = wp.baseurl + Url.getShopListAll + "&mcode=" + wp.c + "&bid=" + sbid + "&aid=" +said
    shopdata = req.get()
    global shoplist
    shoplist = shopdata['data']
    print("shoplist",shoplist)
    return shoplist

def SetEcoShop(sid):
    req.url = wp.baseurl + Url.editship + "&mcode="
    sids = sid.split('|')
    for i in range(len(sids)):
        req.data = "aid={0}&bid={1}&sid={2}&sname={3}&isinvoice={4}&online_time[]={5}&enline_time[]={6}&free_delivery={7}&delivery_markup={8}".format(said,sbid,sids[i],'ces',0)
        print(req.data)

def getSidInfo(bid,aid,sid):
    req.url = wp.baseurl + Url.getShopListAll + "&mcode=" + wp.c + "&bid=" + sbid + "&aid=" + said + "&sid=" + sid
    sidinfo = req.get()
    return sidinfo

