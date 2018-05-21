# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import *
from scrapy import log

class SchoolbooksystemspiderPipeline(object):
    def __init__(self):
        client = MongoClient('mongodb://127.0.0.1/', 27017)
        self.db = client.pythonLessonExamData
        self.collection = self.db.BookData
        self.newCollection = self.db.newBookData
    def process_item(self, item, spider):
        if self.collection.find_one({'_id':item['ISBN']}):
            self.collection.update({'_id':item['ISBN']},{'$set':{'author':item.get('author')}})
        else:
            try:
                self.collection.insert(item)
                # 新书，插入新书表
                self.newCollection.insert(item)
            except Exception as e:
                print('发生了异常:',e)
                print('发生异常时的item是:',item)
                print('数据库已有的Item是',self.db.schoolBookdata.find_one({'_id':item['_id']}))
        return item
