import random

import requests
from lxml.html import etree


def getRandomAlphet():
    result = ''
    for i in range(1,20):
        result += (chr(random.randint(0,24)+65))
    return result
# 获取秘钥
def getSecretKey():
    keyUrl = 'http://opac.szpt.edu.cn:8991/F/'+getRandomAlphet()
    print('url:' + keyUrl)
    response = requests.get(url=keyUrl)
    response.encoding = 'utf-8'
    
    selector = etree.HTML(response.text)
    secretKey = selector.xpath('//a[contains(text(),"登录")]/@href')[0]

    startIndex = secretKey.find('/F/') + 3
    endIndex = secretKey.find('?')
    secretKey = secretKey[startIndex:endIndex]
    return secretKey

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'UM_distinctid=1633a80bb95339-096e7ba2edcff7-444a022e-144000-1633a80bb9644f; yunsuo_session_verify=91fe09a4c281230cc7ac35a0823ffe12',
    'Host': 'opac.szpt.edu.cn:8991',
    'Origin': 'http://opac.szpt.edu.cn:8991',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
}

data = {
    'func': 'login-session',
    'login_source': 'bor-info',
    'bor_id': '{user}',
    'bor_verification': '{password}',
    'bor_library': 'SZY50',
}

def login(user,password):
    url = 'http://opac.szpt.edu.cn:8991/F/{key}?func=file&file_name=login-session'.format(key=getSecretKey())

    response = requests.get(url,headers=headers)
    response.encoding = 'utf-8'

    selector = etree.HTML(response.text)

    href = selector.xpath('//form/@action')[0]

    data['bor_id'] = data['bor_id'].format(user=user)
    data['bor_verification'] = data['bor_verification'].format(password=password)

    response = requests.post(url=href,headers=headers,data=data)
    response.encoding = 'utf-8'

    selector = etree.HTML(response.text)

    judge = selector.xpath('//td[contains(text(),"借阅历史列表")]//text()')

    data['bor_id'] =  '{user}'
    data['bor_verification'] = '{password}'
    if judge != []:
        return True,response
    else:
        return False,None

if __name__ == "__main__":

    # getRandomAlphet()
    print(login('16240011', '19970904')[1].text)
    # login('16240011', '19970904')

    # login('16240011', '19970904')
    # login('16240011', '19970904')
    # login('16240011', '19970904')
    # login('16240011','19970904')
    # login('16240011','19970904')