# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from awesome_movie.items import MovieItem

class AwesomeMovieSpider(scrapy.spiders.CrawlSpider):
    name = 'awesome-movie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/subject/3011091/']

    rules = (
    	Rule(LinkExtractor(allow = 'https://movie.douban.com/subject/.+/?from=subject-page'),callback='parse_page',follow=True),
    	)

    def parse_page(self, response):
        item = MovieItem()
        item['url'] = response.url
        item['name'] = response.xpath('//*[@id="content"]/h1/span[1]/text()').extract_first()
        item['summary'] = response.xpath('//*[@id="link-report"]/span[1]/span/text()').extract_first()
        item['score'] = response.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()').extract_first()
        yield item