import scrapy
from pymongo import *
import json

class CatalogueSpider(scrapy.Spider):
    name = 'CatalogueSpider'

    url = 'https://www.szlib.org.cn/indexc.php?client=szlib&isbn={}'
    client = MongoClient('mongodb://127.0.0.1/', 27017)
    db = client.SchoolBookData

    cookies = {
        '_pk_ref.1.8720' : '%5B%22%22%2C%22%22%2C1525694954%2C%22http%3A%2F%2Fbook.szdnet.org.cn%2Fgoreadbookgc.jsp%3Fdxid%3D000000347916%26unitid%3D993%26d%3D5960E768CE869933701A396A0F6B7A25%26guanji%3D1%22%5D',
        '_pk_ses.1.8720' : '*',
        '_pk_id.1.8720' : '957379f962e1ebd3.1525694954.1.1525696073.1525694954.'
    }
    def start_requests(self):
        bookList = list(self.db.schoolBookdata.find())
        for i in range(0,37738):
            book = bookList[i]
            ISBN = book['ISBN']
            print(i)
            yield scrapy.Request(url=self.url.format(ISBN),callback=self.parseCatalogue,cookies=self.cookies,meta={'ISBN':ISBN})
    def parseCatalogue(self, response):
        ISBN = response.meta['ISBN']
        data = json.loads(response.text[1:-1])
        catalogue = data['result'].get('catalog','')
        if catalogue != '':
            self.db.schoolBookdata.update({"_id":ISBN},{"$set":{"catalog":catalogue}})
            print('ISBN：',ISBN,'的书籍已经更改完毕')