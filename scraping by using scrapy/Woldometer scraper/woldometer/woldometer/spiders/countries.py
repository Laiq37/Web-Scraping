import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    #start_urls = ['https://www.worldometers.info/world-population/population-by-country/']
    
    def start_requests(self):
        yield scrapy.Request(url = 'https://www.worldometers.info/world-population/population-by-country/',callback=self.parse,headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'})

    def parse(self, response):
        countries = response.xpath("//table[@id='example2']//a")
        
        for country in countries:
            name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()
                
            #clean_link = response.urljoin(link)
                
            #yield scrapy.Request(url = clean_link,callback=self.parse_country)
                
            yield response.follow(url = link,callback=self.parse_country,meta={'name': name},headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'})

    def parse_country(self, response):
        
        name = response.request.meta['name']
        rows = response.xpath("//div[@class='table-responsive'][1]/table[@class='table table-striped table-bordered table-hover table-condensed table-list']//tbody/tr")
        
        for row in rows:
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[2]/strong/text()").get()
            yearly_per_change = row.xpath(".//td[3]/text()").get()
            yearly_no_change = row.xpath(".//td[4]/text()").get()
            migrant_net = row.xpath(".//td[5]/text()").get()
            median_age = row.xpath(".//td[6]/text()").get()
            fertility_rate = row.xpath(".//td[7]/text()").get()
            density = row.xpath(".//td[8]/text()").get()
            urban_pop_per = row.xpath(".//td[9]/text()").get()
            urban_pop = row.xpath(".//td[10]/text()").get()
            country_share_in_word_pop = row.xpath(".//td[11]/text()").get()
            global_pop = row.xpath(".//td[12]/text()").get()
            global_rank = row.xpath(".//td[13]/text()").get()
            userr_agent = response.request.headers["USER-AGENT"]
            

            yield {'name':name,'year':year,'population':population,'User-Agent':userr_agent}