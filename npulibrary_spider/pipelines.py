# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class NpulibraryPipeline(object):

    def process_item(self, item, spider):
        # 连接数据库
        # TODO: 改为 settings.py 中的全局配置模式
        conn = pymysql.connect(
            host='localhost',
            user='root',
            passwd='123456',
            db='npulibrary',
            charset='utf8',
            use_unicode=True
        )
        # 获取游标
        cursor = conn.cursor()
        sql = "INSERT INTO " \
              "book(book_title,book_author,book_press,publish_date,book_isbn,book_theme,book_stock,book_info,book_image_url)" \
              "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        params = (item['title'], item['author'], item['press'], item['publish_date'], item['isbn'],
                  item['theme'], int(item['stock']), item['info'], item['image_url'])
        try:
            cursor.execute(sql, params)
            conn.commit()
        except pymysql.Error:
            print("Error!")
        return item
