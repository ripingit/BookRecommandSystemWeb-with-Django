headers = {
    # 'Referer' : 'https://m.douban.com/search/?query=%E4%BB%8E%E9%9B%B6%E5%BC%80%E5%A7%8B%E5%AD%A6Python%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1' ,
    'Upgrade-Insecure-Requests' : '1' ,
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36' ,
    'X-DevTools-Emulate-Network-Conditions-Client-Id' : 'F827E0D03EF29C636F91CD325A56D56D' ,
}
import requests
from threading import Thread
from lxml.html import etree
def get():
    while True:
        response = requests.get(url="https://m.douban.com/search/?query=%E4%BB%8E%E9%9B%B6%E5%BC%80%E5%A7%8B%E5%AD%A6Python%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1&type=book",
                                headers=headers)
        selector = etree.HTML(response.text)
        print(selector.xpath('//span[@class="subject-title"]//text()'))
if __name__ == "__main__":
    for i in range(1,10):
        Thread(target=get).start()