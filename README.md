此项目的存在是为[npulibrary](https://github.com/DangHT/npulibrary)提供数据

使用[Scrapy](https://scrapy.org/)+MySQL

数据来源：[西北工业大学畅想之星电子图书馆](https://www.cxstar.com/xbgy.htm)

注意，经实践发现：

1. 网站中图书内容是通过JS动态加载而来的，因此若直接通过静态方法是无法获取到全部图书数据的
2. 网站中除首页外，几乎所有链接都是通过转发方式完成跳转，因此地址栏url不变

目前采取的解决方案：

1. 采用 Selenium WebDriver 方法，模拟浏览器发送请求可以等待页面加载完成获取完整数据
2. 若要获取多个学科的数据，需要从首页点击链接获取对应的url地址

使用方法：

1. 安装配置 python3 环境
2. 安装依赖包

```shell script
pip install scrapy
pip install pymysql
```
3. 建立数据表（数据表及部分数据样例已在项目中给出[book.sql](https://github.com/DangHT/npulibrary_spider/blob/master/book.sql)）
4. 修改[MySQL配置信息](https://github.com/DangHT/npulibrary_spider/blob/master/npulibrary_spider/pipelines.py)
5. 修改[start_urls和item['theme']](https://github.com/DangHT/npulibrary_spider/blob/b515cb146f8938f56a23ac9d6c95b7f1b30d0f95/npulibrary_spider/spiders/books_spider.py)爬取指定的学科
6. 在控制台输入
```shell script
scrapy crawl books
```

等待完善：
1. 控制 WebDriver 自动跳转到其他学科页面进行爬取
2. 实现翻页爬取
3. 将MySQL等配置信息重写到settings.py中
