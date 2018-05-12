url = 'http://opac.szpt.edu.cn:8991/F/2VUH8YUHIF191C1Y72X2JL4N9EE92MUMJ82187J1AXHDMF3VUR-54710?func=item-global&doc_library=SZY01&doc_number=001270575'
import requests
from lxml.html import etree
response = requests.get(url)
response.encoding = 'utf-8'
selector = etree.HTML(response.text)
# print(selector.xpath('//td[@class="td1" and contains(preceding-sibling::td[1]//text(),"系统号")]//text()')[0].strip())
print(response.text)
