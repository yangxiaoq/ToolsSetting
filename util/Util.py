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