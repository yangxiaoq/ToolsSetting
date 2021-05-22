from util.HttpRequest import Request
from config import config
import WebPage as wp
from util import Url

req = Request()
sbid,said = "",""

def betastart():
    req.url = wp.baseurl + Url.check
    req.data = wp.dataj
    loginresp = req.post()
    if loginresp == "success":
        shopdata = refresh()
    return shopdata


def refresh():
    req.url = wp.baseurl + "/c/" + wp.c
    req.data = None
    refeshresp = req.get()
    if refeshresp == "success":
        return getBrandList()

def getBrandList():
    req.url = wp.baseurl + Url.getBrandList +"?mcode=" + wp.c
    req.data = wp.dataj
    branresp = req.get()
    print("branresp",branresp)
    return getFRegionList(branresp['data'][0]['id'])

def getFRegionList(bid):
    req.url = wp.baseurl + Url.getFRegionList + "?mcode=" + wp.c + "&bid = " + bid
    FRegionresp = req.get()
    print("FRegionresp",FRegionresp)
    return getShopListAll(bid,FRegionresp['data'][0]['aid'])

def getShopListAll(bid,aid):
    global sbid,said
    sbid = bid
    said = aid
    req.url = wp.baseurl + Url.getShopListAll + "&mcode=" + wp.c + "&bid=" + sbid + "&aid=" +said
    shoplist = req.get()
    print("shoplist",shoplist)
    return shoplist

def SetEcoShop(sid):
    req.url = wp.baseurl + Url.editship + "&mcode="
    sids = sid.split('|')
    req.data =

def getSidInfo(bid,aid,sid):
    req.url = wp.baseurl + Url.getShopListAll + "&mcode=" + wp.c + "&bid=" + sbid + "&aid=" + said + "&sid=" + sid
    sidinfo = req.get()
    return sidinfo

