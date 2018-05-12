import requests
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Length': '84',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': 'UM_distinctid=1633a80bb95339-096e7ba2edcff7-444a022e-144000-1633a80bb9644f; yunsuo_session_verify=91fe09a4c281230cc7ac35a0823ffe12; safedog-flow-item=04BCBBB31CDA3CAAFCE272D4EFCC705E',
    'Host': 'opac.szpt.edu.cn:8991',
    'Origin': 'http://opac.szpt.edu.cn:8991',
    'Referer': 'http://opac.szpt.edu.cn:8991/F/?func=file&file_name=login-session',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
}
# url = 'http://opac.szpt.edu.cn:8991/F/XU22S6IKHJK8FIKH2V9HTVUQFS3D6LPSKKAITV6HSGX1MT2GX7-51214'

data = {
    'func': 'login-session',
    'login_source': 'bor-info',
    'bor_id': '16240011',
    'bor_verification': '19970904',
    'bor_library': 'SZY50',
}
#
# response = requests.post(url=url,headers=headers,data=data)
# response.encoding = 'utf-8'
#
# print(response.text)

from lxml.html import etree
import datetime

def login():
    url = 'http://opac.szpt.edu.cn:8991/F/?func=file&file_name=login-session'
    response = requests.get(url)
    response.encoding = 'utf-8'
    print(response.text)
    selector = etree.HTML(response.text)

    href = selector.xpath('//form/@action')[0]

    response = requests.post(url=href,headers=headers,data=data)
    response.encoding = 'utf-8'

    print(response.text)
    print(response.url)

    for data1 in getBorrowBook(response.url):
        print(data1)
        getBorrowDay(data1[3])
def getBorrowBook(url):
    url = url+'?func=bor-loan&adm_library=SZY50'
    response = requests.get(url=url,headers=headers)
    response.encoding = 'utf-8'

    print(response.text)

    selector = etree.HTML(response.text)

    for subselector in selector.xpath('//tr'):
        bookAttributes =  subselector.xpath('.//td[@class="td1"]/text()')
        if bookAttributes:
            yield bookAttributes
# 获得一本书的借阅期限跟现在所在天数的比较
def getBorrowDay(date):
    year = date[0:4]
    month = date[4:6]
    day = date[6:]
    dates = '{year}-{month}-{day}'.format(year=year,month=month,day=day)
    day1 = datetime.datetime.now()
    day2 = datetime.datetime.strptime(dates,'%Y-%m-%d')

    print((day2-day1).days+1)
if __name__ == "__main__":
    login()
