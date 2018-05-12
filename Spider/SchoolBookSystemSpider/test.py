url = 'http://opac.szpt.edu.cn:8991/F/2VUH8YUHIF191C1Y72X2JL4N9EE92MUMJ82187J1AXHDMF3VUR-51238?func=full-set-set&set_number=017285&set_entry=000001&format=999'
import requests
from lxml.html import etree
response = requests.get(url)
response.encoding = 'utf-8'
selector = etree.HTML(response.text)
print(selector.xpath('//td[@class="td1" and contains(preceding-sibling::td[1]//text(),"系统号")]//text()')[0].strip())

