import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BooktoscrapeSpider(CrawlSpider):
    name = 'booktoscrape'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//li/article[@class='product_pod']/h3/a[@title]"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//li[@class='next']/a"))
    )

    def parse_item(self, response):
        yield {
            'Book Name' : response.xpath("//div[@id='content_inner']/article/div/div/h1/text()").get(),
            'Book Price': response.xpath("//div[@id='content_inner']/article/div/div/p[@class='price_color']/text()").get()
        }
