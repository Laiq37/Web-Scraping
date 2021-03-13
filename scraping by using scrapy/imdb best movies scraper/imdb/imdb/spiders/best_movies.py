import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/search/title/?groups=top_250&sort=user_rating/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//h3[@class='lister-item-header']/a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//div[@class='desc']/a"))
    )

    def parse_item(self, response):
        yield {'Movie Name': response.xpath("//div[@class='title_wrapper']/h1/text()").get().replace('\xa0',''),
               'Year': response.xpath("//div[@class='title_wrapper']/h1/span/a/text()").get(),
               'Duration': response.xpath("normalize-space(//div[@class='title_wrapper']/div[@class='subtext']/time/text())").get(),  
               'genre': " | ".join(response.xpath("//div[@class='title_wrapper']/div[@class='subtext']//span[@class='ghost'][3]/preceding-sibling::a/text()").getall()),   
               'URL':response.url 
        }