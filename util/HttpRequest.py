from util import Util,Url
import requests
class Request(object):

    url = ""
    data = None
    files = None
    headers = None

    def post(self):
        self.getHeaders()
        try:
            r = requests.post(self.url, data=self.data, headers=self.headers, files=self.files)
            return self.response(r)
        except BaseException as e:
            print("请求失败！")

    def get(self):
        self.getHeaders()
        try:
            r = requests.get(self.url, data=self.data, headers=self.headers, files=self.files)
            return self.response(r)
        except BaseException as e:
            print("请求失败！")

    def getHeaders(self):
        h = str(Util.readcookie(3))
        self.headers =None if (self.url.find(Url.check) > -1 ) else {"Content-Type": "application/x-www-form-urlencoded","Cookie":h}

    def response(self,r):
        status_code = r.status_code  # 获取返回的状态码
        set_cookie = requests.utils.dict_from_cookiejar(r.cookies)
        rcookie = Util.readcookie()
        for k, v in set_cookie.items():
            rcookie[k] = v
        Util.writecookie(rcookie)
        if status_code == 200:
            try:
                response_json = r.json()
            except BaseException as e:
                response_json = str(r.text)
                if response_json.find("用户登录") > -1:
                    response_json = "fail"
                else:
                    response_json = "success"
        return response_json  # 返回响应码，响应内容

