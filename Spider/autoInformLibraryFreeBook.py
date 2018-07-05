#======================================
# 馆藏空闲通知爬虫
#======================================

from Spider import loginSpider
import requests
from lxml.html import etree
import re

# 输入图书的分馆位置以及系统号，对该图书进行馆藏空闲查询
# 如果存在空闲图书，返回True，不存在返回False

headers = {
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' ,
    'Accept-Encoding' : 'gzip, deflate' ,
    'Accept-Language' : 'zh-CN,zh;q=0.9' ,
    'Cache-Control' : 'max-age=0' ,
    'Connection' : 'keep-alive' ,
    'Cookie' : 'UM_distinctid=1633a80bb95339-096e7ba2edcff7-444a022e-144000-1633a80bb9644f; yunsuo_session_verify=975c42b75b8dc57fc8c3fab442bd8b59' ,
    'Host' : 'opac.szpt.edu.cn:8991' ,
    'Upgrade-Insecure-Requests' : '1' ,
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36' ,
}

def getFreeBook(branchLibrary,systemNumber):
    url = 'http://opac.szpt.edu.cn:8991/F/{SecretKey}?func=item-global&doc_library=SZY01&doc_number={SystemNumber}'
    secretKey = loginSpider.getSecretKey()
    url = url.format(SecretKey=secretKey,SystemNumber=systemNumber)
    response = requests.get(url=url,headers=headers)
    response.encoding = 'utf-8'

    selector = etree.HTML(response.text)

    xpath = '//tr//td[contains(following-sibling::td[1],"{branchLibrary}") or contains(following-sibling::td[2],"{branchLibrary}")]'.format(
        branchLibrary=branchLibrary)

    result = selector.xpath(xpath)

    resultJson = {
        'free':0,       # 在架上
        'Lent':0,       # 已借出
        'Cataloging':0  #编目中
    }

    for element in result:
        if re.search('借出',element.text):
            resultJson['Lent'] += 1
        if re.search('架上',element.text):
            resultJson['free'] += 1
        if re.search('编目',element.text):
            resultJson['Cataloging'] += 1
    return resultJson

if __name__ == "__main__":
    print(getFreeBook('西丽湖','001235552'))