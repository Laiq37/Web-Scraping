from ..items import QuotetutorialItem
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "Quotes"
    website_url = "http://quotes.toscrape.com/"
    start_urls = [website_url]
    def parse(self, response):
            
        items = QuotetutorialItem()
            
        All_quotes = response.css('.quote')
            
        for quote in All_quotes:
            #extracting data with css selector
            quote_css = quote.css('span.text::text').extract()
            author_css = quote.css("small.author::text").get()
            tag_css = quote.css(".tag::text").extract()
            '''next_page_css = quote.css("li.next a::attr(href)").getall() #when we want to extract all links
                #next_page_css = quote.css("li.next a").attrib["href"] # when single needed'''
                
            #extracting data with xpath
            '''
                title_xpath = quote.xpath("//title/text()").extract()
                quote_xpath = quote.xpath("//span[@class='text']/text()").extract()  
                author_css = quote.xpath("//small[@class='author']/text()").extract()
                next_page_xpath= response.xpath("//li[@class='next']/a/@href").extract()  
                #next_page = quote.xpath("//li[@class='next']/a").xpath("@href").extract() '''
                
            items['Quotes'] = quote_css
            items['Author'] = author_css
            items['Tags'] = tag_css
                
            yield items
                
                # extract extract all the records in form of list
                # getall get all records in form of list
                # get get only single value
            next_page = response.css('.next a::attr(href)').get()
            
            if next_page is not None:
                yield response.follow(next_page, callback = self.parse)
            """try:
                yield response.follow(next_page, callback = self.parse)
            except:
                print('All the data has been scraped')"""