# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GlassesshopItem(scrapy.Item):
    
    Name = scrapy.Field()
    Price = scrapy.Field()
    Link = scrapy.Field()
    Img_Url = scrapy.Field()
    image_urls = scrapy.Field()
    no = scrapy.Field()
