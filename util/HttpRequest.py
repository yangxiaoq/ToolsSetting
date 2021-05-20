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
        print("请求的内容：%s" % self.data)
        print("请求的header：%s" % self.headers)


    def response(self,r):
        status_code = r.status_code  # 获取返回的状态码
        print("获取返回的状态码:%d" % status_code)
        set_cookie = requests.utils.dict_from_cookiejar(r.cookies)
        rcookie = Util.readcookie()
        print("contnet",r)
        for k, v in set_cookie.items():
            rcookie[k] = v
        Util.writecookie(rcookie)
        if status_code == 200:
            try:
                response_json = r.json()
                print("响应内容：%s" % response_json)
            except BaseException as e:
                response_json = "success"
        return response_json  # 返回响应码，响应内容

