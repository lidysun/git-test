# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieDyttItem(scrapy.Item):
    # define the fields for your item here like:
    movie_name = scrapy.Field()
    post_date = scrapy.Field()
    # download_url = scrapy.Field()
