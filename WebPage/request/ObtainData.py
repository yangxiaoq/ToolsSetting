from util.HttpRequest import Request
from config import config
import WebPage as wp
from util import Url
from urllib.parse import urlencode

req = Request()
sbid,said = "",""

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
    return shopdata['data']

def SetEcoShop(*key):
    req.url = wp.baseurl + Url.editship + "?mcode=" + wp.c
    sid = key[0]
    if len(sid) == 0:
        return "请选择门店"
    invoice = key[1]
    free_delivery = key[2]
    delivery_markup = key[3]
    sids = sid.split('|')
    for i in range(len(sids)):
        dsid = eval(sids[i])
        dsid['delivery_markup'] = delivery_markup
        dsid['free_delivery'] = free_delivery
        dsid['isinvoice'] = invoice
        online = str(dsid['online_time']).split(' ')
        coordinates = str(dsid['coordinates'])
        redata = urlencode(dsid)
        for i in range(len(online)):
            redata = redata + '&online_time[]=' + online[i].split('-')[0]+ '&enline_time[]=' + online[i].split('-')[1]
        print(redata)
        req.data = redata
        # req.data = "aid={0}&sid={1}&bid={2}&sname={3}&shop_short=&store_id=&phone={4}&mobile=&city={5}" \
        #            "&address={6}&online_time%5B%5D={7}&enline_time%5B%5D={8}&membertype=&btakeout=0&gwonline=0" \
        #            "&membertype_option=&membertype_other=&shop_order_preminutes=0&nonoid=&bank_card_num=" \
        #            "&bank=&third_code=&baidu_id=&bdwu_id=&meituan_id=&eleme_id=&wsh_id=&" \
        #            "wsh_shop_id={9}&wsh_shop_key={10}&jddj_id=&xks_id=&dada_id=&" \
        #            "delivery_charge={11}&least_sendcharge=0.00&delivery_markup={12}&send_advance=0&box_price=0.00&coordinate=" \
        #            "&glng={13}&glat={14}&send_time=0&free_delivery={15}&large_order=0&remind_time=0&introduction=" \
        #            "&announcement=&remarks=&meituan_sfid=&bingex_id=&csid=&jiaoma_id=&isinvoice={16}&techtrans_id=" \
        #            "&coordinates%5B0%5D%5Btype%5D=CIRCLE&coordinates%5B0%5D%5BpeiStartTime%5D=&" \
        #            "coordinates%5B0%5D%5BpeiEndTime%5D=&coordinates%5B0%5D%5Bdelivery_charge%5D=7" \
        #            "&coordinates%5B0%5D%5Bleast_sendcharge%5D=0&coordinates%5B0%5D%5BdelReason%5D=" \
        #            "&coordinates%5B0%5D%5Bcoordinate%5D=&coordinates%5B0%5D%5Bradius%5D=3000" \
        #            "&third_pos=0&pos_ip=&warning_threshold=&dada_merchant_id=&elm_isv_shop_id=&psid".format(
        #     said,dsid['sid'],sbid,dsid['sname'],dsid['phone'],dsid['city'],dsid['address'],dsid['']
        # )
        # print(req.data)
        setres = req.post()
        print(setres)
    return "修改成功"

def getSidInfo(bid,aid,sid):
    req.url = wp.baseurl + Url.getShopListAll + "&mcode=" + wp.c + "&bid=" + sbid + "&aid=" + said + "&sid=" + sid
    sidinfo = req.get()
    return sidinfo

