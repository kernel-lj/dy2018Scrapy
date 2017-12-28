# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
class Dy2018ScrapyPipeline(object):
        pass

    # def __init__(self):
    #     self.f = open("dy.json", "w")
    #
    # # 有中文要加 ensure_ascii=False
    # def process_item(self, item, spider):
    #
    #     print "8" * 100
    #     print  item
    #
    #     content = json.dumps(dict(item), ensure_ascii=False) + ",\n"
    #     self.f.write(content)
    #     return item
    #
    # def close_spider(self, spider):
    #     self.f.close()

