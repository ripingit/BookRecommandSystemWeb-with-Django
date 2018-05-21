from pymongo import *
class MyDataBase(object):
    def __init__(self):
        self.client = MongoClient('mongodb://127.0.0.1', 27017)
        self.db = self.client.pythonLessonExamData
        self.collections = self.db.BookData
        #====================================
        # userData:
        #   {
        #       'userName':xxx,
        #       'password':xxx,
        #       'commonTags':{
        #           'tags1':'使用次数1',
        #           ..................
        #       },
        #       'email':'xxxx',
        #       简单说明一下特别关注的字段，特别关注字段里面是一个字典，
        #       字典一共有n个键，分别是目录，内容简介，书名，等等，
        #       每个字段里面包含一个列表，列表里面是用户设置的特别关注的标签。
        #       'CatalogKey':['Unity','Shader',.......],
        #       'BookNameKey':[''],
        #       'BookAuthorKey':[''],
        #       'BookPublisherKey':['']
        #       'isAutoBorrow':'true|False',
        #       'isNewBook':'true|False'
        #       ''
        #   }
        #+===================================
        self.userData = self.db.userData
    # 查看用户是否是第一次登录，如果是，那么返回true，否则返回false
    def isFirstLogin(self,userName):
        if self.userData.find_one({'userName':userName}):
            return False
        else:
            return True
    # 查看用户是否已经设置了邮箱,True表示设置了
    def hasEmail(self,userName):
        try:
            data = self.userData.find_one({'userName':userName})
            if data.get('email',None):
                return True
            else:
                return False
        except:
            return False
    def hasTags(self,userName):
        try:
            data = self.userData.find_one({'userName':userName})
            if data.get('commonTags',None):
                return True
            else:
                return False
        except:
            return False

