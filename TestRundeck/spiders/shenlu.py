# -*- coding: utf-8 -*-
import scrapy


class ShenluSpider(scrapy.Spider):
    name = 'shenlu'
    allowed_domains = ['www.shenlu007.com']
    start_urls = ['http://www.shenlu007.com/']

    def parse(self, response):
        pass
