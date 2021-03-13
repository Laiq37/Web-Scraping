from ..items import AmazonbotItem
import scrapy

class Amazonbot(scrapy.Spider):
    name = 'amazon_bot'#bot name
    
    search_term = input('Search Product: ')
    
    start_urls = [f'https://www.amazon.com/s?k={search_term}']#site url list
    
    def parse(self, response):
        
        items = AmazonbotItem()
        
        records = response.xpath('//div[@data-component-type="s-search-result"]')
        
        for record in records:
        
            p_name = record.css('.a-size-medium::text').get()
            p_rating = record.css('span.a-icon-alt::text').get()
            p_reviews = record.css('a span.a-size-base::text').get()
            p_price = record.css('span.a-price span.a-offscreen::text').get()
            p_link = 'www.amazon.com'+record.css('h2 a::attr(href)').get()
            
            items['name'] = p_name
            items['rating'] = p_rating
            items['review'] = p_reviews
            items['price'] = p_price
            items['link'] = p_link
            
            yield items
            
        next_page = response.css('li.a-last a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page,callback = self.parse)