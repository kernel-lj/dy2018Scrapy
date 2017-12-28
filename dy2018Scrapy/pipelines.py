# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
class Dy2018ScrapyPipeline(object):
    def __init__(self):
        self.f = open("dy.text", "w")

    # 有中文要加 ensure_ascii=False
    def process_item(self, item, spider):
        self.f.write(item['down_link'].encode('utf8') + '\n')
        return item

    def close_spider(self, spider):
        self.f.close()

