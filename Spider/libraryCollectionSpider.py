import requests
from threading import Thread
url = 'http://opac.szpt.edu.cn:8991/F/UFFTQANJKV42U7PPP2A2C3GEMGFU9FJI97HEKVICVTIER3M8K4-31950?func=item-global&doc_library=SZY01&doc_number=001276944'
headers = {
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' ,
    'Accept-Encoding' : 'gzip, deflate' ,
    'Accept-Language' : 'zh-CN,zh;q=0.9' ,
    'Cache-Control' : 'max-age=0' ,
    'Connection' : 'keep-alive' ,
    'Cookie' : 'UM_distinctid=1633a80bb95339-096e7ba2edcff7-444a022e-144000-1633a80bb9644f; yunsuo_session_verify=920b73f4499b2ff4e5ab6b8dd4bd0d8d' ,
    'Host' : 'opac.szpt.edu.cn:8991' ,
    'Upgrade-Insecure-Requests' : '1' ,
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36' ,
}
def get():
    while True:
        response = requests.get(url=url,headers=headers)
        response.encoding = 'utf-8'
        print(response.text)

if __name__ == "__main__":
    for i in range(1,10):
        Thread(target=get).start()