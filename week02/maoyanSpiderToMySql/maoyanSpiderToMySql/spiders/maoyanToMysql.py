# -*- coding: utf-8 -*-
import scrapy
from week2.assignment.maoyanSpiderToMySql.maoyanSpiderToMySql.items import MaoyanspiderItem

class MaoyantomysqlSpider(scrapy.Spider):
    # 这里的name 当执行命令的时候会与name关联
    name = 'maoyanToMysql'

    # allowed_domains = ['maoyan.com']
    # start_urls = ['https://maoyan.com/films?showType=3']

    #测试是否使用代理IP begin
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/ip']
    # 测试是否使用代理IP end

    # def start_requests(self):
    #     for i in range(0,10):
    #         url = f'https://maoyan.com/films?showType=3&offset={i*30}'
    #         yield scrapy.Request(url = url,callback=self.parse,dont_filter=False)

    # print("---------------")

    # def parse(self, response):
    #     print(response.text)

    def parse(self, response):
        items = []
        # print(response.body.decode())
        #print(response.text)
        i = 0
        top = 10
        for each in response.xpath('//div[@class="movie-hover-info"]'):
            if (i < top):
                item = MaoyanspiderItem()
                # print(each)
                title = each.xpath('div[2]/@title').extract_first().strip()
                category = each.xpath('div[2]/text()[2]').extract_first().strip()
                date = each.xpath('div[4]/text()[2]').extract_first().strip()

                item['title'] = title  # .encode('utf-8')
                item['category'] = category  # .encode('utf-8')
                item['date'] = date  # .encode('utf-8')

                items.append(item)
                # print(item)
                i += 1
            else:
                break
            yield item

        # return items
