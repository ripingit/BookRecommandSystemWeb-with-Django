#=================================
# 获取代理ip（于西刺代理处）
#================================
import requests
from lxml.html import etree
class ProxiesSpider(object):
    def __init__(self):
        self.url = 'http://www.xicidaili.com/wn/{page}'     # 西刺代理URL
        self.verificationUrl = 'https://icanhazip.com/'
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Cookie': '_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWM5NjAzOGNkZTA2Njg3Yzg0MDBiNDJmMGYzOWE5NmIwBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMVVqMlQ4RVNQQlVpTVAwRDNHWjE5SDFsUXp5c3V4c0hMdXdzd3BDZm92a3M9BjsARg%3D%3D--59d01b9be3faedccb119a123b97a129b24a217e7',
            'Host': 'www.xicidaili.com',
            'Referer': 'http://www.xicidaili.com/wn/3',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        }
        self.proxiesSet = set()     # 保存已经爬过的proxies，避免重复爬取
        self.page = 1       # 目前已经爬到的页数
        self.totalPage = 1000
    def getProxies(self):
        while self.page<=self.totalPage:
            url = self.url.format(page=self.page)
            response = requests.get(url=url,headers=self.headers)
            selector = etree.HTML(response.text)
            trs = selector.xpath('//tr[@class]')
            for tr in trs:
                result = tr.xpath('.//td/text()')
                https = result[0]
                port = result[1]
                proxiesUrl = https + ':' + port

                if proxiesUrl in self.proxiesSet:
                    continue

                proxies = {
                    'https': proxiesUrl
                }
                try:
                    print('正在获取代理ip')
                    proxiesResponse = requests.get(url=self.verificationUrl,proxies=proxies,timeout=40)
                    self.proxiesSet.add(proxiesUrl)
                    return proxies
                except:
                    pass
            self.page += 1
            if self.page >= 1000:
                self.page = 0
                self.proxiesSet.clear()
proxiesspider = ProxiesSpider()