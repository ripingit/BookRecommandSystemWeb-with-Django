# 对Mongodb进行数据清理，所有需要排序的字段，
# 通通转换成相应的数字类型，同时，如果，
# 不存在该字段，自动给该字段赋默认值-1

from pymongo import *
import re
client = MongoClient('mongodb://127.0.0.1',27017)
db = client.pythonLessonExamData
collection = db.BookData
count = db.BookData.find().count()
for skip in range(0, count + 1, 1000):
    print(skip)
    books = list(db.BookData.find().limit(1000).skip(skip))
    for bookData in books:
        ISBN = bookData.get('ISBN')
        print(ISBN)
        try:
            publishYear = int(bookData.get('publishYear',-1))
        except:
            publishYear = -1
        publisher = None
        if bookData.get('publisher', '暂无').find(':')!=-1 or bookData.get('publisher', '暂无').find(',')!=-1:
            try:
                publisher = re.split(':|,',bookData.get('publisher', '暂无'))[1].strip()
            except:
                publisher = '暂无'
        try:
            ratingAverage = float(bookData.get('ratingAverage',-1))
        except:
            ratingAverage = -1
        try:
            ratingNumberRaters = int(bookData.get('ratingNumberRaters',-1))
        except:
            ratingNumberRaters = -1
        if publisher:
            collection.update({'ISBN':ISBN},
                              {'$set':{
                                  'publishYear':publishYear,
                                  'publisher':publisher,
                                  'ratingAverage':ratingAverage,
                                  'ratingNumberRaters':ratingNumberRaters}
                              })
        else:
            collection.update({'ISBN': ISBN},
                              {'$set': {
                                  'publishYear': publishYear,
                                  'ratingAverage': ratingAverage,
                                  'ratingNumberRaters': ratingNumberRaters}
                              })