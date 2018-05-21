from apscheduler.schedulers.background import BackgroundScheduler
from Spider import *
from Spider.autoBarrowBookSpider import *
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
import Spider.SchoolBookSystemSpider.SchoolBookSystemSpider.items
from Spider.SchoolBookSystemSpider.SchoolBookSystemSpider.spiders import *
from Spider.SchoolBookSystemSpider.SchoolBookSystemSpider.pipelines import SchoolbooksystemspiderPipeline

from Pyemail.emailManger import *

from scrapy.settings import Settings

class Scheduled:
    borrowSched = BackgroundScheduler()
    newBookSched = BackgroundScheduler()
    newBookUserSched = BackgroundScheduler()
    def __init__(self):
        self.newBookAuto()
        self.start()
    def start(self):
        self.borrowSched.start()
        self.newBookSched.start()
        self.newBookUserSched.start()
    # 为borrowSched增加一项自动续借的任务
    def addAutoBorrow(self,userName,password,receivers):
        self.borrowSched.add_job(wholeAutoBorrow,'interval',days=1,args=(userName,password,receivers),name='{}-job'.format(userName))
    # 为newBookUserSched增加一项新书速递的任务
    def addAutoNewBook(self,userName):
        pass
    # 在外部运行scrapy
    def startScrapyWithExtern(self):
        sttings = Settings({
            'SPIDER_MODULES': ['Spider.SchoolBookSystemSpider.SchoolBookSystemSpider.spiders.BookSpider'],
            'ROBOTSTXT_OBEY': False,
            'ITEM_PIPELINES': {
                'Spider.SchoolBookSystemSpider.SchoolBookSystemSpider.pipelines.SchoolbooksystemspiderPipeline': 300,
            }
        })
        runner = CrawlerRunner(settings=sttings)
        d = runner.crawl('BookSpider')
        d.addBoth(lambda _: reactor.stop())
        reactor.run()
    def newBookAuto(self):
        self.newBookSched.add_job(self.startScrapyWithExtern,'interval',weeks=4)
# 单例
scheduled = Scheduled()
