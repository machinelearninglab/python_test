# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from myspider.items import MyspiderItem


class JluSpider(CrawlSpider):
    name = 'jlu'
    allowed_domains = ['jlu.edu.cn']
    start_urls = ['http://news.jlu.edu.cn/jdxw/xykx.htm']

    rules = [
        # xykx/66.htm
        Rule(LinkExtractor(allow=[r'xykx/\d+\.htm']), callback='', follow=True, ),
        # https://news.jlu.edu.cn/info/1021/49072.htm
        Rule(LinkExtractor(allow= r'../info/.*'), callback='parse_item', follow=True, )
    ]

    def parse_item(self, response):

            item = MyspiderItem()

            title = response.xpath('//div[@class = "content-title fl"]/h2/text()').extract()
            name = response.xpath('//div[@class = "content-title fl"]/span/a/text()').extract()
            info = response.xpath('//div[@class = "content-con fl"]/p/text()').extract()

            item['name'] = name[1]
            item['time'] = name[0]
            item['title'] = title[0]
            item['info'] = info

            yield item
