from util.HttpRequest import Request
from config import config
import WebPage as wp
from util import Url,Util
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

def getShopParam(sid):
    req.url = wp.baseurl + Url.loadshop_param.format(wp.c,str(sid))
    shoppar = req.get()
    global savesidconf
    savesidconf = shoppar['data']
    print(savesidconf)
    return shoppar

def SetEcoShop(*key):
    urllist = []
    datalist = []
    jburl = wp.baseurl + Url.editship + "?mcode=" + wp.c
    sid = key[0]
    if len(sid) == 0:
        return '{"success":"2","msg":"请选择门店"}'
    invoice = key[1]
    free_delivery = key[2]
    delivery_markup = key[3]
    is_online = key[4]
    sel_week = key[5]
    devtime = key[6]
    timerule = key[7]
    sel_buss = key[8]
    online_time = key[9]
    if sel_buss == "":
        return '{"success":"2","msg":"请选择经营方式"}'
    sids = sid.split('|')
    savesid = ""
    for i in range(len(sids)):
        dsid = eval(sids[i])
        savesid += dsid['sid']
        if len(sids) > 1 and i != len(sids)-1:
            savesid += ","
        dsid['delivery_markup'] = delivery_markup
        dsid['free_delivery'] = free_delivery
        dsid['isinvoice'] = invoice
        online_time = str(online_time).strip()
        if bool(online_time) == False:
            online_time = "00:00-23:59"
        online = online_time.split(',')
        if type(dsid['coordinates']) not in [tuple,list]:
            coordinates = eval(dsid['coordinates'])
        else:
            coordinates = dsid['coordinates']
        dsid.pop('online_time')
        dsid.pop('coordinates')
        redata = urlencode(dsid)
        starttimelist = []
        endtimelist = []
        istimenormal = True
        for i in range(len(online)):
            try:
                starttime = online[i].strip().split('-')[0]
                endtime = online[i].strip().split('-')[1]
                starttime,isbreak = Util.matchtime(starttime,1)
                endtime,isbreak = Util.matchtime(endtime,2)
            except BaseException as e:
                starttime = "00:00"
                endtime = "23:59"
                isbreak = True
            finally:
                starttimelist.append(starttime)
                endtimelist.append(endtime)
            if isbreak:
                break

        istimenormal = Util.isTimeNormal(starttimelist,endtimelist)
        if istimenormal:
            for itime in range(len(starttimelist)):
                redata += '&online_time[]=' + starttimelist[itime] + '&enline_time[]=' + endtimelist[itime]
        else:
            redata += '&online_time[]=' + "00:00" + '&enline_time[]=' + "23:59"
        for j in range(len(coordinates)):
            coorob = coordinates[j]
            for k,v in coorob.items():
                redata += "&coordinates["+str(j)+"]["+k+"]=" + str(v)
        urllist.append(jburl)
        datalist.append(redata)

    # 修改门店配置
    saveshopurl = wp.baseurl + Url.saveConfigStore.format(savesid,wp.c)
    savesidconf['auto_receive_order'] = is_online
    savesidconf['business_type'] = sel_buss
    savesidconf['dinrange'] = sel_week
    savesidconf['intervaltime'] = devtime
    savesidconf['dinrule'] = timerule
    #比对加入
    savesidconf["order_invoice"] = savesidconf["orderInvoice"]
    savesidconf.pop("is_writePos")
    savesidconf.pop("orderInvoice")
    savesidconf.pop("is_invoice")
    savesidconf.pop("is_eco_delivery")
    savesidconf.pop("delivery")
    savesidconf.pop("bd_source_id")
    urllist.append(saveshopurl)
    datalist.append(savesidconf)

    setres = req.grequest(urllist,datalist)
    return setres

savesidconf = {}

def getSidInfo(bid,aid,sid):
    req.url = wp.baseurl + Url.getShopListAll + "&mcode=" + wp.c + "&bid=" + sbid + "&aid=" + said + "&sid=" + sid
    sidinfo = req.get()
    return sidinfo

