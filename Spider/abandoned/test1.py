import pymysql

# 创建连接
conn = pymysql.connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       password='09043330',
                       db='test',
                       charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor)
conn.autocommit(True)
with conn.cursor() as cursor:
    result = cursor.execute(query='update just_a_test set test="bb" where test="aaaa"')
    print(cursor.fetchall())

