import pymysql

class DatabaseComment(object):
    def __init__(self):
        self.user = 'root'
        self.password = '09043330'
    def getConnection(self,user,password):
        connection = pymysql.connect(host='127.0.0.1',
                                          port=3306,
                                          user=user,
                                          password=password,
                                          db='booksystemdatawithjava',
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)
        return connection

    # 查询,返回
    def queryComments(self, ISBN:str):

        sql = 'select * from comments where fromISBN={}'.format(ISBN)
        resultStr = ""

        connection = self.getConnection(self.user, self.password)
        cursor = connection.cursor()
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            for data in result:
                resultStr += data['comment']+" "
        except:
            pass
        finally:
            cursor.close()
            connection.close()
        return resultStr

    # 根据用户ID，返回目标用户的密码与邮箱
    def queryUser(self,userID:str):
        sql = 'select * from users where userName={}'.format(userID)

        connection = self.getConnection(self.user, self.password)
        cursor = connection.cursor()

        user = {}

        try:
            cursor.execute(sql)
            result = cursor.fetchone()
            user['userName'] = result['userName']
            user['password'] = result['password']
            user['email'] = result['email']
        except:
            pass
        finally:
            cursor.close()
            connection.close()
        return user