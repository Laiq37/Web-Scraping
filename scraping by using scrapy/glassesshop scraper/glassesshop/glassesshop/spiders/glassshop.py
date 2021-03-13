from ..items import GlassesshopItem
import re
import scrapy
from time import sleep

class GlassshopSpider(scrapy.Spider):
    name = 'glassshop'
    allowed_domains = ['www.glassesshop.com/bestsellers']
    start_urls = ['https://www.glassesshop.com/bestsellers','https://www.glassesshop.com/bestsellers?page=2','https://www.glassesshop.com/bestsellers?page=3','https://www.glassesshop.com/bestsellers?page=4','https://www.glassesshop.com/bestsellers?page=5']

    def parse(self, response):
        items = GlassesshopItem()
        
        results = response.css('.product-list-row.product-list-item')
        for no, item in enumerate(results):
            if item.css('.ad-banner'):
                continue
            
            link = item.css('.product-list-row.product-list-item a.product-img::attr(href)').get()
            img_link = item.css('.product-img-outer img.d-block.product-img-default::attr(data-src)')
            raw_name = item.css('.product-list-row.product-list-item .p-title-block .p-title a::text').get()
            name = re.sub('[\\n\s]','',raw_name)
            price = item.css('.product-list-row.product-list-item .p-title-block .p-price span::text').get()
            
            items['Name'] = name 
            items['Price'] = price
            items['Link'] = link
            items['Img_Url'] = img_link.get()
            items['image_urls'] = img_link.getall()
            items['no'] = no+1
                
            yield items
