from DataBaseManagement.database import MyDataBase
from django import template
# 返回邮箱是否已经设置的标签，
# 如果已经设置，返回邮箱，
# 如果没有，返回None
register = template.Library()

@register.simple_tag
def getEmail(username):
    try:
        mydatabase = MyDataBase()
        data = mydatabase.userData.find_one({'userName': username})
        mydatabase.client.close()
        email = data.get('email', None)
        if email and len(email)>0:
            return email
        else:
            return None
    except:
        return None
@register.simple_tag
def getTags(username):
    try:
        mydatabase = MyDataBase()
        data = mydatabase.userData.find_one({'userName': username})
        mydatabase.client.close()

        key = {
            'BookNameKey':data.get('BookNameKey',[]),
            'BookAuthorKey':data.get('BookAuthorKey',[]),
            'CatalogKey':data.get('CatalogKey',[]),
            'BookPublisherKey':data.get('BookPublisherKey',[])
        }

        resultList = []

        for name,value1 in key.items():
            for value2 in value1:
                if name == 'BookNameKey':
                    catalog = '题名'
                elif name == 'BookAuthorKey':
                    catalog = '著者'
                elif name == 'CatalogKey':
                    catalog = '目录'
                elif name == 'BookPublisherKey':
                    catalog = '出版社'
                else:
                    catalog = '题名'
                keystr = value2 + '({catalog})'.format(catalog=catalog)
                resultList.append(keystr)

        return resultList
    except:
        return None