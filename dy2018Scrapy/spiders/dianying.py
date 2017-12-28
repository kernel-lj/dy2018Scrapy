# -*- coding: utf-8 -*-
import scrapy


class DianyingSpider(scrapy.Spider):
    def __init__(self):
        self.f = open("dy.text", "a+")

    name = "dianying"
    allowed_domains = ["dy2018.com"]
    start_urls = ["http://www.dy2018.com/html/gndy/dyzz/index.html"]


    def parse(self, response):
        node_list = response.xpath("//table[@class='tbspan']")
        links = node_list.xpath(".//tr[2]//td[2]//b//a/@href").extract()

        for link in links:
            url = "http://www.dy2018.com" + link
            yield scrapy.Request(url, callback=self.parse1)

    def parse1(self, response):
        node_list = response.xpath("//*[@id='Zoom']/table[1]//tr[1]/td/a/text()").extract()
        self.f.write(node_list[0].encode('utf8') + '\n')


