from django.db import models

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





