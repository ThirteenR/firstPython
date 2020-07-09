import urllib.request
import http.cookiejar


class getcontent:
    url = "https://blog.csdn.net/doudou19930614/article/details/83022308"

    def __init__(self, url=url):
        self.url = url

    def simplerequest(self):
        print('简单请求')
        response = urllib.request.urlopen(self.url)
        return response.read()

    def headerrequest(self):
        print('伪装请求头')
        request = urllib.request.Request(self.url)
        request.add_header("user-agent", "Mozilla/5/0")
        response1 = urllib.request.urlopen(self.url)
        return response1.read()

    def cookierequest(self):
        print('第三种')
        cj = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        urllib.request.install_opener(opener)
        response2 = urllib.request.urlopen(self.url)
        return response2.read()
