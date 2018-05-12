# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SchoolbooksystemspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Book(scrapy.Item):
    _id = scrapy.Field()
    # 书名
    bookName = scrapy.Field()
    # 作者
    author = scrapy.Field()
    # 索书号
    index = scrapy.Field()
    # 出版社
    publisher = scrapy.Field()
    # 出版年份
    publishYear = scrapy.Field()
    # ISBN码
    ISBN = scrapy.Field()
    # 内容简介
    content = scrapy.Field()
    # 目录
    catalogue = scrapy.Field()
    # 分类
    Class = scrapy.Field()
    # 书本的真实url
    bookUrl = scrapy.Field()
    # 书本的图像地址
    imagePath = scrapy.Field()
    # 馆藏地址
    bookEmptyUrl = scrapy.Field()
    # 系统号
    systemNumber = scrapy.Field()