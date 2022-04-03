import scrapy

class TagsSpider(scrapy.Spider):
    name = 'tag'
    start_urls = ['https://quotes.toscrape.com/'] 
    
    def parse(self, response):
       divs = response.css('.quote')
       for div in divs:
           tags = div.css('.tag::text').getall()
           yield{
             'tag':tags
           }
           
       
    

