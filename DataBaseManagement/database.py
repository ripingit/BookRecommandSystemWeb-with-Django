from pymongo import *
class MyDataBase(object):
    def __init__(self):
        self.client = MongoClient('mongodb://127.0.0.1', 27017)
        self.db = self.client.pythonLessonExamData
        self.collections = self.db.BookData