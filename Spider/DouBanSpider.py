import requests
from pymongo import *
import time
#=================================================================
# 豆瓣分布式爬虫(分布式方案废弃)
#================================================================


#==================================================================
# MongoDb队列
#==================================================================
# class UrlQueue(object):
#     def __init__(self,client):
#         self.db = client.pythonLessonExamData
#         self.collection = self.db.urlQueue
#         self.waitDownload = 'WAITDOWNLOAD'
#         self.finishedDownload = 'FINISHEDDOWNLOAD'
#     def pop(self):
#         result = self.collection.find_and_modify(
#             query={
#                 'status':self.waitDownload
#             },
#             update={
#                 '$set':{
#                     'status': self.finishedDownload
#                 }
#             }
#         )
#         try:
#             return result['url']
#         except:
#             return None

#=================================================================
# 豆瓣分布式爬虫程序
#=================================================================
class DouBanSpider(object):
    def __init__(self):
        self.url = 'https://api.douban.com/v2/book/isbn/:{ISBN}'
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'bid=A5msJzzDJtw; gr_user_id=10d4e140-0254-4138-85da-7ab7e871eb69; _vwo_uuid_v2=D4ECDB5F078128A995CD3C86C70F69894|bfd8aff0c9034137ebe13aa5104f642d; ap=1; ct=y; ll="118282"; __utmz=30149280.1525700180.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; regpop=1; __utma=30149280.1745519780.1525694828.1526021235.1526025182.7; __utmc=30149280; __utmt=1; __utmt_douban=1; viewed="10561367_3811448_25880388_1206755_1230487_27154117_1533752_1282071_1677734"; __utmb=30149280.19.10.1526025182',
            'Host': 'api.douban.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
        }
        self.client = MongoClient('mongodb://39.108.176.18/', 27017)
        self.db = self.client.pythonLessonExamData
        self.collection = self.db.BookData
        self.file = open('douBanSpider.log','w+',encoding='utf-8')
    def start_request(self):
        count = self.db.BookData.find().count()
        for skip in range(0,count+1,100):
            self.file.write('skip:'+str(skip)+'\n')
            self.file.flush()
            books = list(self.db.BookData.find().limit(100).skip(skip))
            for bookData in books:
                ISBN = bookData['ISBN']
                url = self.url.format(ISBN=ISBN)
                response = requests.get(url=url,headers=self.headers)
                data = response.json()
                author = data.get('author','暂无')
                doubanId = data.get('id','暂无')
                rating = data.get('rating',None)
                if rating:
                    ratingAverage = data['rating'].get('average','暂无')
                    ratingNumberRaters = data['rating'].get('numRaters','暂无')
                else:
                    ratingAverage = '暂无'
                    ratingNumberRaters = '暂无'
                doubanSummary = data.get('summary','暂无')
                series = data.get('series',None)
                if series:
                    seriesTitle = series.get('title','暂无')
                else:
                    seriesTitle = '暂无'

                # 获得ISBN码
                startindex = url.rfind(':')+1
                ISBN = url[startindex:]

                self.collection.update({'_id':ISBN},
                                       {
                                           '$set':{
                                               'author':author,
                                               'doubanId':doubanId,
                                               'ratingAverage':ratingAverage,
                                               'ratingNumberRaters':ratingNumberRaters,
                                               'doubanSummary':doubanSummary,
                                               'seriesTitle':seriesTitle
                                            }
                                        })
                time.sleep(3.5)
if __name__ == "__main__":
    spider = DouBanSpider()
    spider.start_request()