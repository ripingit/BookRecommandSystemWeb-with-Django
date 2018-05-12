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
            'Connection': 'keep-alive',
            'Cookie': 'bid=A5msJzzDJtw; gr_user_id=10d4e140-0254-4138-85da-7ab7e871eb69; _vwo_uuid_v2=D4ECDB5F078128A995CD3C86C70F69894|bfd8aff0c9034137ebe13aa5104f642d; __yadk_uid=Vq9o4tS9Re6OHcE4DzDGeFsh1CW5wnNM; ap=1; ct=y; ll="118282"; _pk_ref.100001.3ac3=%5B%22%22%2C%22%22%2C1525700193%2C%22https%3A%2F%2Fwww.douban.com%2Fsearch%3Fq%3D%25E6%25B8%25B8%25E6%2588%258F%25E4%25BA%25BA%25E5%25B7%25A5%25E6%2599%25BA%25E8%2583%25BD%22%5D; _pk_id.100001.3ac3=9df06291dc4281ae.1525694828.2.1525700200.1525696187.; ps=y; __utmz=30149280.1526058285.11.5.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; viewed="26945534_10561367_1474667_3811448_25880388_1206755_1230487_27154117_1533752_1282071"; __utma=30149280.1745519780.1525694828.1526058285.1526095981.12; __utmc=30149280; __utmt=1; dbcl2="173434188:cpnj9z6Fnqg"; ck=XZdP; __utmt_douban=1; __utmb=30149280.3.10.1526095981; __utma=81379588.917288980.1525694828.1526058285.1526096294.12; __utmc=81379588; __utmz=81379588.1526096294.12.10.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/accounts/login; __utmb=81379588.1.10.1526096294; push_noty_num=0; push_doumail_num=0',
            'Host': 'book.douban.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36',
        }
        self.client = MongoClient('mongodb://39.108.176.18/', 27017)
        self.db = self.client.pythonLessonExamData
        self.collection = self.db.BookData
        self.file = open('douBanSpider.log','w+',encoding='utf-8')
    def start_request(self):
        count = self.db.BookData.find().count()
        for skip in range(300,count+1,100):
            self.file.write('skip:'+str(skip)+'\n')
            self.file.flush()
            books = list(self.db.BookData.find().limit(100).skip(skip))
            for bookData in books:
                ISBN = bookData['ISBN']
                url = self.url.format(ISBN=ISBN)
                # response = requests.get(url=url,headers=self.headers)
                data = self.get(url=url)
                self.file.write('data:'+str(data)+'\n')
                self.file.flush()

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

    def get(self,url):
        while True:
            response = requests.get(url=url, headers=self.headers)
            data = response.json()
            if data.get('msg','') == 'rate_limit_exceeded2: 39.108.176.18':
                time.sleep(600)
            else:
                return data


if __name__ == "__main__":
    spider = DouBanSpider()
    spider.start_request()