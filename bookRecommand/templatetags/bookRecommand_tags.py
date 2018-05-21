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
        if data.get('email', None):
            return data.get('email', None)
        else:
            return None
    except:
        return None