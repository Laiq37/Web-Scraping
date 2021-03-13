from ..items import EcommercebotItem
import scrapy

class CzoneSpider(scrapy.Spider):
    
    name = "czone_bot"  # bot name
    
    search_term = input('Seacrh product : ') # product, we want to search
    
    tot_res = 0
    
    start_urls = [f'https://www.czone.com.pk/search.aspx?kw={search_term}'] #website from where the spider will crawl data
    
    def parse(self, response):
        
        items = EcommercebotItem()
        
        results = response.css('#divListView div.template')
        
        for result in results:
            
            p_category = result.css('.product-data-title::text').get() + result.css('.product-data::text').get()
            
            if CzoneSpider.search_term+" ".casefold() not in p_category.casefold():
                continue
            
            p_name = result.css('h4 a::text').get()
            
            if CzoneSpider.search_term+" ".casefold() not in p_name.casefold():
                continue
            
            p_category = result.css('.product-data-title::text').get() + result.css('.product-data::text').get() 
            
            p_rating = result.css('.star_rating::text').get()
            
            p_price = result.css('.price span::text').get()   
            
            p_link = 'https://www.czone.com.pk' + result.css('h4 a::attr(href)').get()      
            
            CzoneSpider.tot_res = CzoneSpider.tot_res + 1
            
            items['Name'] = p_name
            items['Category'] = p_category
            items['Rating'] = p_rating
            items['Link'] = p_link
            items['Price'] = p_price
            
            yield items
        
        next_page = response.css('.NextPage::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback = self.parse)
        else:
            print("Match Found: ",CzoneSpider.tot_res) # total no. of searhc product found on website