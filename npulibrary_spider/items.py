# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NpulibraryItem(scrapy.Item):
    title = scrapy.Field()          # 书名
    author = scrapy.Field()         # 作者
    press = scrapy.Field()          # 出版社
    publish_date = scrapy.Field()   # 出版日期
    isbn = scrapy.Field()           # ISBN
    theme = scrapy.Field()          # 主题
    info = scrapy.Field()           # 简介
    image_url = scrapy.Field()      # 封面图片链接
    stock = scrapy.Field()          # 库存量
