# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EcommercebotItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Name = scrapy.Field()
    Rating = scrapy.Field()
    Category = scrapy.Field()
    Price = scrapy.Field()
    Link = scrapy.Field()
