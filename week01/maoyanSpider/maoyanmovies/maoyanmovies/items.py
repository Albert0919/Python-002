# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanmoviesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 接收movies  Spider的值
    movies_name = scrapy.Field()
    movies_type = scrapy.Field()
    movies_date = scrapy.Field()
