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
    name = 'jlu1'
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

            item = WeiboItem()

            title = response.xpath('//div[@class = "content-title fl"]/h2/text()').extract()
            name = response.xpath('//div[@class = "content-title fl"]/span/a/text()').extract()
            info = response.xpath('//div[@class = "content-con fl"]/p/text()').extract()

            item['name'] = name[1]
            item['time'] = name[0]
            item['title'] = title[0]
            item['info'] = info

            yield item

#pipelines
import csv
import os
from pandas import DataFrame

class WeiboPipeline(object):

    def __init__(self):
        # csv文件的位置,无需事先创建
        store_file = os.path.dirname(__file__) + '/jlu_result.csv'
        # 打开(创建)文件
        self.file = open(store_file, 'w', newline='')
        # csv写法
        self.writer = csv.writer(self.file)

    def process_item(self, item, spider):
        # 判断字段值不为空再写入文件
        if item['name']:
            self.writer.writerow([item['time'],item['name'],item['title'],item['info']])
        return item

    def close_spider(self, spider):
        # 关闭爬虫时顺便将文件保存退出
        self.file.close()

#cutwc        
import jieba
import matplotlib.pyplot as plt
from os import path
from pandas import read_csv, Series
from wordcloud import WordCloud

df = read_csv('jlu_result.csv',encoding='gbk',header = None, names=['time','auth','title','content'])
#print(df.head())
d = path.dirname(__file__)
mydic = {}

for i in range(0, len(df)):
    older = ''
    #print(x)
    # print(df.iloc[i]['time'])
    if mydic.__contains__(df.iloc[i]['time']):
        older = mydic[df.iloc[i]['time']]
    content = ' '.join(df.iloc[i]['content'])
    content = content.replace('\\', '').replace(' ', '').replace('rn', '').replace('[', '').replace(']', '').replace('"', '').replace("'", '')
    newer = older + content
    mydic[df.iloc[i]['time']] = newer

for time in mydic:
    word_list = ' '.join(jieba.cut(mydic[time]))
    wordcloud = WordCloud(font_path='simhei.ttf',
                      width = 800,
                      height = 600,
                      background_color='white').generate(word_list)
    plt.imshow(wordcloud)
    plt.show()
    wordcloud.to_file(path.join(d, time+".png"))