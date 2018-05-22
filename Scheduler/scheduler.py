from apscheduler.schedulers.background import BackgroundScheduler
from Spider import autoBarrowBookSpider
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from DataBaseManagement.database import MyDataBase
import Spider.SchoolBookSystemSpider.SchoolBookSystemSpider.items
from Spider.SchoolBookSystemSpider.SchoolBookSystemSpider.spiders import *
from Spider.SchoolBookSystemSpider.SchoolBookSystemSpider.pipelines import SchoolbooksystemspiderPipeline

from Pyemail import emailManger

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
        self.borrowSched.add_job(autoBarrowBookSpider.wholeAutoBorrow,'interval',days=1,args=(userName,password,receivers),name='{}-job'.format(userName))
    # 为newBookUserSched增加一项新书速递的任务
    def addUserAutoNewBook(self,userName):
        self.newBookUserSched.add_job(self.newBookForUserAuto,'interval',weeks=5)
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

    # 为读者进行自动的新书速递功能
    def newBookForUserAuto(self,userName,receivers):
        mydatabase = MyDataBase()

        # 第一步，获得用户表中的数据
        data = mydatabase.userData.find_one({'userName': userName})

        # 第二步，获得用户的邮箱
        email = data.get('email',None)

        # 保存用户关注的新书
        resultBooks = []

        if email:
            # 获得该用户的所有特别关注标签
            CatalogKey = data.get('CatalogKey', [])
            BookNameKey = data.get('BookNameKey', [])
            BookAuthorKey = data.get('BookAuthorKey', [])
            BookPublisherKey = data.get('BookPublisherKey', [])
            for key in CatalogKey:
                findData = {'catalog':{'$regex':key}}
                datas = mydatabase.db.newBookData.find(findData)
                for book in datas:
                    resultBooks.append(book)
            for key in BookNameKey:
                findData = {'bookName':{'$regex':key}}
                datas = mydatabase.collections.find(findData)
                for book in datas:
                    resultBooks.append(book)
            for key in BookAuthorKey:
                findData = {'author': {'$regex': key}}
                datas = mydatabase.collections.find(findData)
                for book in datas:
                    resultBooks.append(book)
            for key in BookPublisherKey:
                findData = {'publisher': {'$regex': key}}
                datas = mydatabase.collections.find(findData)
                for book in datas:
                    resultBooks.append(book)

            # 发送邮件
            bookstr = ''.join(['<li><p> 书名:' + book['bookName']+ ' ISBN号:'+book['ISBN']+' </p> </li>' for book in resultBooks])
            content = '''
                <p>图书馆有一批新书~~~:</p>
                <p>下面为您推送您特别关注的新书:</p>
                <ul>
                    {bookContent}
                </ul>
            '''.format(bookContent=bookstr)
            emailManger.sendEmail(content=content, title='图书借阅系统', receivers=receivers)
        mydatabase.client.close()
# 单例
scheduled = Scheduled()
