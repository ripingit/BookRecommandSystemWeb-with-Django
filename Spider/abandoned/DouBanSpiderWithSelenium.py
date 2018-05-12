from selenium import webdriver
from lxml.html import etree
from pymongo import *
import time

#=====================================
# 豆瓣Selenium爬虫（方案已废弃）
#======================================

class DouBanSpiderWithSelenium(object):
    def __init__(self):
        self.client = MongoClient('mongodb://39.108.176.18/', 27017)
        self.db = self.client.pythonLessonExamData
        self.collection = self.db.BookData
        self.driver = webdriver.Chrome(executable_path='D:\\phantomjs\\chromedriver.exe')
        self.file = open('douBanSpider.log','w+',encoding='utf-8')
        self.cookie = {
            'bid': 'A5msJzzDJtw',
            'gr_user_id': '10d4e140-0254-4138-85da-7ab7e871eb69',
            '_vwo_uuid_v2': 'D4ECDB5F078128A995CD3C86C70F69894|bfd8aff0c9034137ebe13aa5104f642d',
            '__yadk_uid': 'Vq9o4tS9Re6OHcE4DzDGeFsh1CW5wnNM',
            'ap': '1',
            'ct': 'y',
            'll': '"118282"',
            '_pk_ref.100001.3ac3': '%5B%22%22%2C%22%22%2C1525700193%2C%22https%3A%2F%2Fwww.douban.com%2Fsearch%3Fq%3D%25E6%25B8%25B8%25E6%2588%258F%25E4%25BA%25BA%25E5%25B7%25A5%25E6%2599%25BA%25E8%2583%25BD%22%5D',
            '_pk_id.100001.3ac3': '9df06291dc4281ae.1525694828.2.1525700200.1525696187.',
            'ps': 'y',
            '__utmz': '30149280.1526058285.11.5.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
            'viewed': '"26945534_10561367_1474667_3811448_25880388_1206755_1230487_27154117_1533752_1282071"',
            '__utma': '30149280.1745519780.1525694828.1526058285.1526095981.12',
            '__utmc': '30149280',
            '__utmt': '1',
            'dbcl2': '"173434188:cpnj9z6Fnqg"',
            'ck': 'XZdP',
            '__utmt_douban': '1',
            '__utmb': '30149280.3.10.1526095981',
            '__utma': '81379588.917288980.1525694828.1526058285.1526096294.12',
            '__utmc': '81379588',
            '__utmz': '81379588.1526096294.12.10.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/accounts/login',
            '__utmb': '81379588.1.10.1526096294',
            'push_noty_num': '0',
            'push_doumail_num': '0',
        }
    def getBook(self,ISBN):
        self.driver.get(url='https://book.douban.com/')

        inputElement = self.driver.find_elements_by_xpath('//input[@id="inp-query"]')[0]

        inputElement.send_keys(ISBN)

        searchElement = self.driver.find_elements_by_xpath('//div[@class="inp-btn"]/input[@type="submit"]')[0]

        searchElement.click()
        result = (self.driver.find_elements_by_xpath('//div[@class="detail"]/div[@class="title"]/a'))[0]

        result.click()

        return self.driver.page_source
    def parseBook(self,response,ISBN):
        selector = etree.HTML(response)
        # 内容简介
        try:
            intro = (''.join(selector.xpath('//div[@class="intro"]//text()'))).strip()
        except:
            intro = ''
        # 豆瓣评分
        try:
            rating = selector.xpath('//strong[contains(@class,"rating_num")]//text()')[0]
        except:
            rating = ''
        # 豆瓣评分人数
        try:
            ratingNum = selector.xpath('//div[@class="rating_sum"]//span[@property="v:votes"]/text()')[0]
        except:
            ratingNum = ''

        self.file.write('data:' + str(intro) + '\n')
        self.file.flush()

        if rating!='':
            self.collection.update({'_id': ISBN},
                                   {
                                       '$set': {
                                           'ratingAverage': rating,
                                           'ratingNumberRaters': ratingNum,
                                           'doubanSummary': intro,
                                       }
                                   })
    def startRequests(self):
        count = self.db.BookData.find().count()
        for skip in range(300, count + 1, 100):
            self.file.write('skip:'+str(skip)+'\n')
            self.file.flush()
            books = list(self.db.BookData.find().limit(100).skip(skip))
            for bookData in books:
                ISBN = bookData['ISBN']
                self.file.write('data:'+str(ISBN)+'\n')
                self.file.flush()
                try:
                    response = self.getBook(ISBN)
                    self.parseBook(response,ISBN)
                except:
                    pass
                time.sleep(40)


if __name__ == "__main__":
    a = DouBanSpiderWithSelenium()
    # response = a.getBook('9787121306594')
    # a.parseBook(response)
    a.startRequests()