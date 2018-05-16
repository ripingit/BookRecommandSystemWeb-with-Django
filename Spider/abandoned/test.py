from pymongo import *
client = MongoClient('mongodb://127.0.0.1/', 27017)
db = client.pythonLessonExamData
collection = db.BookData

if __name__ == "__main__":
    print(client)
    count = 0
    for data in collection.find():
        if not data.get('doubanId',None):
            count += 1
            print(count)
