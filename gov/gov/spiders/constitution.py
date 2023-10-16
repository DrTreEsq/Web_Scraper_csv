import scrapy
# INSTEAD OF XPATH - 
from whiskyscraper.items import WhiskyscraperItem
from scrapy.loader import ItemLoader

#THIS IS FOR XPATH
import os
from os.path import dirname


class ConstitutionSpider(scrapy.Spider):
    name = "constitution"
    allowed_domains = ["constitutioncenter.org"]
    start_urls = ["https://constitutioncenter.org/the-constitution/full-text"]

    def parse(self, response):
        for articles in response.css('article.article_body'):
            l = ItemLoader(item = WhiskyscraperItem(), selector=products)

            l.add_css('name', 'a.product-item-link')
            l.add_css('price', 'span.price')
            l.add_css('link', 'a.product-item-link::attr(href)')

            yield l.load_item()


        next_page = response.css('a.action.next').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)%
            
            
# Azure - PostgreSQL, instead of JSON
# css instead of xpath