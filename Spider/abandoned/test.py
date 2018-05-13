from pymongo import *
client = MongoClient('mongodb://39.108.176.18/', 27017)
db = client.pythonLessonExamData
collection = db.BookData

if __name__ == "__main__":
    print(client)
    count = 0
    for data in collection.find():
        print(data)
        if not data.get('systemNumber',None):
            count += 1
            print(count)
            print(data)