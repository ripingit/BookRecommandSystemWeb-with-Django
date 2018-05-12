import scrapy

class DouBanSpider(scrapy.Spider):
    name = 'DouBanSpider'
    def start_requests(self):
        print('start！！！')
        yield scrapy.Request(url='https://www.baidu.com')