# -*- coding: utf-8 -*-
import scrapy
import os
from dy2018Scrapy.items import Dy2018ScrapyItem


class DianyingSpider(scrapy.Spider):
    name = "dianying"
    allowed_domains = ["dy2018.com"]

    base_url = "http://www.dy2018.com/html/gndy/dyzz/"
    offset = 1
    trail_url = "index_" + str(offset) + ".html"
    if trail_url == "index_1.html":
        trail_url = 'index.html'

    start_urls = [base_url + trail_url]

    def parse(self, response):
        node_list = response.xpath("//table[@class='tbspan']")
        links = node_list.xpath(".//tr[2]//td[2]//b//a/@href").extract()

        for link in links:
            url = "http://www.dy2018.com" + link
            yield scrapy.Request(url, callback=self.parse1)

        # 296是最后一页 +=1是下一页 将下面if代码注释打开可以爬取下一页的电影链接 296是总页数(也是最后一页)
            # 比如http://117.169.20.240:9090/html/gndy/dyzz/index_296.html
            # 打开下面的代码不会爬取所有的电影，因为电影天堂早期的网页代码和现在有区别，在次我没有做适配，也很简单,
            # 不适配也能抓取一两千的电影链接
        # if self.offset <= 296:
        #     self.offset += 1
        #     self.trail_url = "index_" + str(self.offset) + ".html"
        #     yield scrapy.Request(self.base_url + self.trail_url, callback=self.parse)

    def parse1(self, response):
        item = Dy2018ScrapyItem()
        node_list = response.xpath("//*[@id='Zoom']/table[1]//tr[1]/td/a/text()").extract()
        item['down_link'] = node_list[0]
        yield item


