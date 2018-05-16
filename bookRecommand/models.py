from django.db import models
from django import forms
from Spider import loginSpider
# Create your models here.

class Book(models.Model):
    # ISBN码
    ISBN = models.CharField(max_length=100,null=True)
    # 书名
    bookName = models.TextField(null=True)
    # 书籍URL
    bookUrl = models.CharField(max_length=200,null=True)
    # 作者
    author = models.CharField(max_length=200,null=True)
    # 内容简介
    content = models.TextField(default="",null=True)
    # 出版日期
    publishYear = models.CharField(max_length=50,null=True)
    # 索书号
    bookIndex = models.CharField(max_length=50,null=True)
    # 出版社
    publisher = models.CharField(max_length=100,null=True)
    # 目录
    catalog = models.TextField(null=True)
    # 系统号
    systemNumber = models.CharField(max_length=50,default="0",null=True)
    # 豆瓣ID
    douBanId = models.CharField(max_length=50,default="0",null=True)
    # 豆瓣评分
    doubanRating = models.FloatField(default=0,null=True)
    # 豆瓣评分人数
    doubanRatingPeron = models.IntegerField(default=0,null=True)
    # 丛书系列标题
    seriesTitle = models.CharField(max_length=70,default="",null=True)
    # 豆瓣内容摘要
    doubanSummary = models.TextField(default="",null=True)
    def __str__(self):
        return 'name[{name}]'.format(name=self.bookName)


#====================================
# 登录表单
#====================================
class LoginForm(forms.Form):
    user = forms.CharField(label='user',max_length=100)
    password = forms.CharField(label='password',max_length=100)
    def is_valid(self):
        if loginSpider.login(self.data['user'],self.data['password'])[0]:
            return True
        else:
            return False