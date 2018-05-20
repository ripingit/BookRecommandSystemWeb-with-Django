import requests
from pymongo import *
import time

#=================================================================
# 豆瓣爬虫
#=================================================================
from Spider.getProxies import proxiesspider
class DouBanSpider(object):
    def __init__(self):
        self.url = 'https://api.douban.com/v2/book/isbn/:{ISBN}'
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'bid=A5msJzzDJtw; gr_user_id=10d4e140-0254-4138-85da-7ab7e871eb69; _vwo_uuid_v2=D4ECDB5F078128A995CD3C86C70F69894|bfd8aff0c9034137ebe13aa5104f642d; ap=1; ct=y; ll="118282"; ps=y; push_noty_num=0; push_doumail_num=0; __utmv=30149280.17343; __utma=30149280.1745519780.1525694828.1526216918.1526364967.18; __utmc=30149280; __utmz=30149280.1526364967.18.7.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; regpop=1; viewed="27608477_27073447_27136947_26945534_10561367_1474667_3811448_25880388_1206755_1230487"',
            'Host': 'api.douban.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36',
        }
        self.client = MongoClient('mongodb://127.0.0.1/', 27017)
        self.db = self.client.pythonLessonExamData
        self.collection = self.db.BookData
        self.proxies = None
        self.file = open('douBanSpider.log','w+',encoding='utf-8')
        self.proxiesspider = proxiesspider
    def start_request(self):
        count = self.db.BookData.find().count()
        for skip in range(10700,count+1,100):
            self.file.write('skip:'+str(skip)+'\n')
            self.file.flush()
            books = list(self.db.BookData.find().limit(100).skip(skip))
            for bookData in books:
                ISBN = bookData['ISBN']
                url = self.url.format(ISBN=ISBN)
                data = self.get(url=url)

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
            try:
                if self.proxies:
                    response = requests.get(url=url, headers=self.headers,proxies=self.proxies)
                else:
                    response = requests.get(url=url, headers=self.headers)
            except:
                response = requests.get(url=url, headers=self.headers)
                print('将代理ip置为空')
                self.proxies = None
            data = response.json()
            if data.get('msg','').find('rate_limit_exceeded2')!=-1:
                print(data)
                if self.proxies:
                    print('将代理ip置为空')
                    self.proxies = None
                    time.sleep(120)
                else:
                    print('获取新的代理ip')
                    self.proxies = next(self.proxiesspider.getProxies())
                    print('得到的新代理ip是:',self.proxies)
                    continue
            else:
                return data


if __name__ == "__main__":
    spider = DouBanSpider()
    spider.start_request()