import random

import scrapy

from npulibrary_spider.items import NpulibraryItem
from selenium import webdriver


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["cxstar.com"]
    start_urls = [
        # 这里填写需要抓取的学科分类链接
        # TODO:改为页面到首页的自动跳转
        "https://www.cxstar.com/Book/SubjectNav?pinst=20b1affe000001XXXX&type=bg&navruid=1d39451c001cc50bce",
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.browser = webdriver.Chrome()

    def __del__(self):
        self.browser.close()

    # TODO:添加翻页爬取
    def parse(self, response):
        self.browser.get(response.url)
        books = self.browser.find_elements_by_css_selector(".book-list-item")
        for book in books:
            item = NpulibraryItem()

            title = book.find_element_by_css_selector(".book-list-content > div.list_title.list_maxwidth > a").text
            author = book.find_element_by_css_selector(".book-list-content > div.listbook-author > a").text
            press = book.find_element_by_css_selector(".book-list-content > div.book-publisher > a").text
            publish_date = book.find_element_by_css_selector(
                ".book-list-content > div.book-publisher > div:nth-child(3)").text
            isbn = book.find_element_by_css_selector(".book-list-content > div.book-publisher > div:nth-child(4)").text
            info = book.find_element_by_css_selector(".book-list-content > div.book-intro > p").text
            image_url = book.find_element_by_css_selector(".book-list-cover > a > img").get_attribute("src")
            # image_url = book.find_element_by_xpath("//div[@class=\"book-list-cover\"]//a//img").get_attribute("src")

            item["title"] = title
            item["author"] = author
            item["press"] = press
            item["publish_date"] = publish_date[5:]
            item["isbn"] = isbn[5:]
            item["info"] = info[0:100] + '...'
            item["image_url"] = image_url
            # 根据学科分类链接，手动改写学科类别
            # TODO:改为从页面自动获取学科类别
            item["theme"] = "工学"
            item["stock"] = random.randint(1, 10)

            yield item
