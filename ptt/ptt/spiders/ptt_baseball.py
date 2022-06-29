import scrapy
from ptt.items import PttPostItem
import time 

class PttBaseballSpider(scrapy.Spider):
    name = 'ptt_baseball'
    allowed_domains = ['ptt.cc']
    start_urls = ['https://www.ptt.cc/bbs/Baseball/index.html']

    def parse(self, response):
        next_page = response.css('.wide::attr(href)').getall()[1]
        posts = response.css('.r-ent')
        for post in posts :
            item = PttPostItem()
            title = post.css('.title a::text').get()
            author = post.css('.author::text').get()
            date = post.css('.date::text').get()
            url = post.css('.title a::attr(href)').get()
            print(title, author, date, url)
            item['title'] = title
            item['author'] = author
            item['date'] = date
            item['url'] = url
            yield item
        print(next_page)
        time.sleep(3)
        yield response.follow(next_page,  self.parse)


