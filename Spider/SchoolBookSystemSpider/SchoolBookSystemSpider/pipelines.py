# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import *
from scrapy import log

class SchoolbooksystemspiderPipeline(object):
    def __init__(self):
        client = MongoClient('mongodb://39.108.176.18/', 27017)
        self.db = client.pythonLessonExamData
        self.collection = self.db.BookData
    def process_item(self, item, spider):
        if self.collection.find_one({'_id':item['ISBN']}):
            self.collection.update(
                {'_id':item['ISBN']},
                {
                    '$set':{
                        'systemNumber':item['systemNumber']
                    }
                })
        else:
            try:
                self.collection.insert(item)
            except Exception as e:
                print('发生了异常:',e)
                print('发生异常时的item是:',item)
                print('数据库已有的Item是',self.db.schoolBookdata.find_one({'_id':item['_id']}))
        return item
