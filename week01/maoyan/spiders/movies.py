# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from maoyan.items import MaoyanItem

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

#    def parse(self, response):
#        pass

    def start_requests(self):
        url = self.start_urls[0]
        #url = 'https://maoyan.com/films?showType=3'
        print("url==="+url)

        yield scrapy.Request(url=url, callback=self.parse, dont_filter=False)


    def parse(self,response):
        print(response.url)
        print(response.text)
        # movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        # for i in range(10):
        #     movie = movies[i]
        #     item = MaoyanItem()
        #     title = movie.xpath('./div[1]/span[1]/text()').extract()[0]
        #     movie_type = movie.xpath('./div[2]/text()[2]').extract()[0].strip()
        #     release_date = movie.xpath('./div[4]/text()[2]').extract()[0].strip()
        #     item['title'] = title
        #     item['movie_type'] = movie_type
        #     item['release_date'] = release_date
        #     yield item
        print(response.url)
        # movies = Selector(response=response).xpath('//div[@class="channel-detail movie-item-title"]')
        movies = Selector(response=response).xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd[2]/div[2]')
        for movie in movies: 
            item = MaoyanItem()
            title = movie.xpath('./a/text()')
            link =  movie.xpath('./a/@href')
            item['title'] = title.extract_first().strip()
            item['link'] = 'https://' + self.allowed_domains[0] + link.extract_first().strip()
            yield scrapy.Request(url=item['link'],meta={'item': item},callback=self.parse2)


    def parse2(self,response):
        """  
        到对应标题的链接中获取电影信息
        """
        item = response.meta['item']
        infos = Selector(response=response).xpath('//div[@class="movie-brief-container"]')
        print(infos)
        for info in infos:
            category = info.xpath('./ul/li/a/text()').extract()
            date = info.xpath('./ul/li[last()]/text()').extract_first().strip()
            item['category'] = category
            item['date'] = date

        yield item