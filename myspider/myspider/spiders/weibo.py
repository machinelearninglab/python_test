# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from myspider.items import MyspiderItem


class WeiboSpider(CrawlSpider):
    name = 'weibo'
    allowed_domains = ['m.weibo.cn']
    start_urls = ['https://m.weibo.cn/u/1191220232/']

    rules = (
        Rule(LinkExtractor(allow=r'https://m.weibo.cn/u/1191220232/.*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        content_list = response.xpath('//div[@class = "card-main"]')

        for content in content_list:
            item = MyspiderItem()

            name = content.xpath('./header/div/div/h4/span[@class = "time"]/text()').extract()
            title = content.xpath('./header/div/div/h4/span[@class = "from"]/text()').extract()
            info = content.xpath('./article/div/div[@class = "weibo-text"]/text()').extract()

            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]

            yield item
