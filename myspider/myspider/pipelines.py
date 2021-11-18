# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import os


class MyspiderPipeline(object):
    def __init__(self):
        # csv文件的位置,无需事先创建
        store_file = os.path.dirname(__file__) + '/weibo_result.csv'
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

