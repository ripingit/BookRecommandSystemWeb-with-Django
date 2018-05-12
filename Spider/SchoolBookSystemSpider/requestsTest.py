import requests
from threading import Thread
from lxml.html import etree

# def get():
#     while True:
#         url = 'https://www.szlib.org.cn/Search/searchshow.jsp?v_tablearray=bibliosm%2Cserbibm%2Capabibibm%2Cmmbibm%2C&v_index=isbn&v_value=9787111581666++&cirtype=&v_startpubyear=&v_endpubyear=&v_publisher=&v_author=&sortfield=score&sorttype=desc'
#         response = requests.get(url=url)
#
#         selector = etree.HTML(response.text)
#
#         print(selector.xpath("//a[@name='detail']/text()"))
#
if __name__ == "__main__":
    url = 'http://opac.szpt.edu.cn:8991/F/?func=find-b&request=A1?&&jump=1'
    response = requests.get(url)
    response.encoding = 'utf-8'
    print(response.text)