import re

s = "hello World!"

print(s.capitalize())
print(s.lower())
print(s.upper())

print(s.count('o', 5))
print(s.find('o', 5))

s1 = '{0} and {1} are best {word1} {word2} in the world!'
print(s1.format('Python', 'Java', word1='programming', word2='language'));

s1_array = ['Python', 'and','Java', 'are', 'best', 'programming', 'language', 'in', 'the', 'world!']
print(' '.join(s1_array))

s2 = '   ssss AAAA ssss    '
print(s2.strip())
print(s2.lstrip().lstrip('s'))
print(s2.rstrip().lstrip('s'))

print(s2.replace(' ', '_'))
print(s2.strip().split(sep=' ', maxsplit=-1))
#re test
print(re.match('^\d{3}\-\d{3,8}$', '010-123456'))
if re.match(r'^\d{3}\\\d{3,8}$', r'010\123456'):
    print('OK')
else:
    print('failed')

print(re.split(r'\s+', 'a   b c     d'))
print(re.split(r'[\s\,]+', 'a,   b, c     d'))
print(re.split(r'[\s\,\;]+', 'a,   b;; c,     d'))

# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from weibo.items import WeiboItem


class ExampleSpider(CrawlSpider):
    name = 'jlu'
    allowed_domains = ['jlu.edu.cn']
    start_urls = ['https://news.jlu.edu.cn/jdxw/xykx/66.htm']
    rules = [
        # xykx/66.htm
        Rule(LinkExtractor(allow=r'xykx/\d+\.htm*'), callback='parse_item', follow=True,)
    ]

    def parse_item(self, response):
        content_list = response.xpath('//div[@class = "list-news-left fl"]/ul/li')

        for content in content_list:
            item = WeiboItem()
            name = content.xpath('./span/text()').extract()
            title = content.xpath('./a/text()').extract()
            info = content.xpath('./a/@href').extract()

            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]

            yield item
