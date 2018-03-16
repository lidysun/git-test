# -*- coding:utf-8 -*-
import scrapy
from scrapy.http import Request
from movie_dytt.items import MovieDyttItem

class movieSpider(scrapy.Spider):
    name = 'movie_spider'
    allowed_domain = ['ygdy8.com']
    first_urls = ['http://www.ygdy8.com/html/gndy/rihan/list_6_1.html']
    
    def parse(self, response):
        movies = response.xpath('//div[@class="co_content8"]/ul/table[@class="tbspan"]')
        for li in movies:
            item = MovieDyttItem()
            item['movie_name'] = li.xpath('./tbody/tr[2]/td[2]/b/a[@class="ulink"]').extract()[0]
            item['post_date'] = li.xpath('./tbody/tr[3]/td[2]/font').extract()[0]
            print item
            yield item