import pymongo
import pymysql

mongoClient = pymongo.MongoClient('mongodb://127.0.0.1/',27017)
db = mongoClient.pythonLessonExamData
mySqlClient = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='09043330',
    db='booksystemdata',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor)

cursor = mySqlClient.cursor()
# 循环获得Mongodb的数据
count = db.BookData.find().count()
# cursor.execute('insert into bookrecommand_book(ISBN,content) values(%s,%s)',('123456','''
#     这是一多行的文本
#     有多个行
# '''))
mySqlClient.commit()
for skip in range(14200, count + 1, 100):
    # print(skip)
    books = list(db.BookData.find().limit(100).skip(skip))
    for bookData in books:
        try:
            doubanRating = int(bookData.get('ratingAverage',0))
        except:
            doubanRating = 0
        try:
            doubanRatingPerson=float(bookData.get('ratingNumberRaters', 0))
        except:
            doubanRatingPerson=0
        catalog = bookData.get('catalog', '暂无').replace('\'','')
        catalog = catalog.replace('\"', '')
        content = bookData.get('content', '暂无')
        content = content.replace('\'','')
        content = content.replace('\"', '')
        doubanSummary = bookData.get('doubanSummary', '暂无')
        doubanSummary = doubanSummary.replace('\'','')
        doubanSummary = doubanSummary.replace('\"', '')
        author = ','.join(bookData.get('author', '暂无'))
        author = author.replace('\'','')
        author = author.replace('\"', '')
        bookName = bookData.get('bookName', '暂无')
        bookName = bookName.replace('\'','')
        bookName = bookName.replace('\"', '')
        insertSql = 'insert into bookrecommand_book(' \
                    'ISBN,' \
                    'bookName,' \
                    'bookUrl,' \
                    'author,' \
                    'content,' \
                    'publishYear,' \
                    'bookIndex,' \
                    'publisher,' \
                    'catalog,' \
                    'douBanId,' \
                    'doubanRating,' \
                    'doubanRatingPeron,' \
                    'doubanSummary,' \
                    'seriesTitle,' \
                    'systemNumber' \
                    ') ' \
                    'values(' \
                    '"{ISBN}",' \
                    '"{bookName}",' \
                    '"{bookUrl}",' \
                    '"{author}",' \
                    '"{content}",' \
                    '"{publishYear}",' \
                    '"{bookIndex}",' \
                    '"{publisher}",' \
                    '"{catalog}",' \
                    '"{douBanId}",' \
                    '{doubanRating},' \
                    '{doubanRatingPerson},' \
                    '"{doubanSummary}",' \
                    '"{seriesTitle}",' \
                    '"{systemNumber}"' \
                    ')'.\
            format(
                ISBN=bookData.get('ISBN','暂无'),
                bookName=bookName,
                bookUrl=bookData.get('bookUrl','暂无'),
                author=author,
                content=content,
                publishYear=bookData.get('publishYear','暂无'),
                bookIndex=bookData.get('index','暂无'),
                publisher=bookData.get('publisher','暂无'),
                catalog=catalog,
                douBanId=bookData.get('doubanId','暂无'),
                doubanRating=doubanRating,
                doubanRatingPerson=doubanRatingPerson,
                doubanSummary=doubanSummary,
                seriesTitle=bookData.get('seriesTitle','暂无'),
                systemNumber=bookData.get('systemNumber','暂无')
            )
        # print(insertSql)
        cursor.execute(insertSql)
        mySqlClient.commit()
