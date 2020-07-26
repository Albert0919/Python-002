import scrapy
import lxml.etree
from maoyanmovies.items import MaoyanmoviesItem
from scrapy.selector import Selector


class MoviesSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    # 解析URL并且获取相应数据
    def parse(self, response):
        items = []
        # 定义电影名称空列表
        name_list = []
        # 定义电影类型空列表
        type_list = []
        # 定义上映时间空列表
        date_list = []
        item = MaoyanmoviesItem()
        # 获取根节点
        movies_info = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        for i in range(0, 10):
            # 根据前导根节点获取电影名称
            if i == 5:
                name_list.append(movies_info[i].xpath(
                    './div[@class="movie-hover-title"]/span[@class="name noscore"]/text()').extract())
            else:
                name_list.append(movies_info[i].xpath('./div[@class="movie-hover-title"]/span[@class="name "]/text()').extract())
            item['movies_name'] = name_list

        for i in range(0, 10):
            # 根据前导根节点获取电影类型
            type_list.append(movies_info[i].xpath('(./div[@class="movie-hover-title"]/span[@class="hover-tag"])[1]/../text()').extract())
            item['movies_type'] = type_list
            # 根据前导根节点获取上映时间
            date_list.append(movies_info[i].xpath('(./div[@class="movie-hover-title movie-hover-brief"]/span[@class="hover-tag"])/../text()').extract())
            item['movies_date'] = date_list

        # 将获取的数据添加到item列表中
        items.append(item)
        return items



