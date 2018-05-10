from django.db import models
from django import forms
from Spider import loginSpider
# Create your models here.

class Book(models.Model):
    ISBN = models.CharField(max_length=100)
    bookName = models.CharField(max_length=100)
    bookUrl = models.CharField(max_length=100)
    author = models.CharField(max_length=20)
    content = models.TextField()
    publishYear = models.CharField(max_length=20)
    index = models.CharField(max_length=20)
    publisher = models.CharField(max_length=40)
    catalog = models.TextField()

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