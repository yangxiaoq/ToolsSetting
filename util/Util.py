import os

cookiefile = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'config','cookie.txt')

def writecookie(cookies):
    with open(cookiefile ,"w",encoding="utf-8") as f:
        f.write('%s'%cookies)
        f.close()

def readcookie(type = 2):
    with open(cookiefile, "r", encoding="utf-8") as f:
        content = f.read()
        if content == '':
            cookievalue = {}
        else:
            cookievalue = eval(content)
        if type != 2:
            cookievaluet = ""
            for k,v in cookievalue.items():
                cookievaluet = '%s=%s;%s'%(k,v,cookievaluet)
                cookievalue = cookievaluet[0:-1]
    return cookievalue

cfile = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'config','c.txt')

def writec(c):
    with open(cfile ,"w",encoding="utf-8") as f:
        f.write('%s'%c)
        f.close()

def readc():
    with open(cfile, "r", encoding="utf-8") as f:
        content = f.read()
    return content


def differencelist():
    string1 = "bd_source_id=&auto_receive_order=0&true_printer=0&invoice=0&tender=0&comment_reply=0&fapei_time=0&pos_type=0&delivery=-1&wjd_confirm=0&shop_pos_url=&is_eco_delivery=1&income_type=0&dinrange=1%2C3%2C5%2C6%2C7&intervaltime=10&paytype=1%2C2&dinrule=2&tzx_print=0&payqr=0&deliverytypes=&isautodelivery=1&business_type=1&enjoy_activity=&orderInvoice=2&dinstime=00%3A00&dinetime=00%3A00&bd_source_name=&is_writePos=&is_invoice=1&order_invoice=2"
    string2 = "auto_receive_order=0&bd_source_name=&isautodelivery=1&deliverytypes=&true_printer=0&wjd_confirm=0&pos_type=0&shop_pos_url=&invoice=0&order_invoice=2&tender=0&comment_reply=0&income_type=&tzx_print=0&payqr=0&fapei_time=0&enjoy_activity=&business_type=1&paytype=1%2C2&dinrange=1%2C3%2C6%2C7&intervaltime=10&dinrule=2&dinstime=00%3A00&dinetime=00%3A00"
    list1 = string1.split("&")
    list2 = string2.split("&")
    list3 = list(set(list2).difference(set(list1)))
    print('%s'%list3)
    list4 = list(set(list1).difference(set(list2)))
    print('%s' % list4)

