
import requests
class Request(object):

    url = ""
    data = None
    headers = None
    files = None

    def post(self):
        try:
            r = requests.post(self.url, data=self.data, headers=self.headers, files=self.files)
            print("请求的内容：%s" % self.data)
            status_code = r.status_code  # 获取返回的状态码
            print("获取返回的状态码:%d" % status_code)
            response_json = r.json()  # 响应内容，json类型转化成python数据类型
            print("响应内容：%s" % response_json)
            return status_code, response_json  # 返回响应码，响应内容
        except BaseException as e:
            print("请求失败！", exc_info=1)

