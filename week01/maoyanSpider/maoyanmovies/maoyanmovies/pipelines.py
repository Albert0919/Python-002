# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pandas as pd


class MaoyanmoviesPipeline:

    def process_item(self, item, spider):
        # 定义电影信息列表
        movies_info = []
        # 定义电影名称空列表
        movies_name = []
        # 设定电影类型空列表
        type_datas = []
        # 设定电影上映时间空列表
        date_datas = []
        # 接收movies传递的值
        movie_name = item['movies_name']
        movie_type = item['movies_type']
        movie_date = item['movies_date']

        # 遍历电影名称
        for datas in movie_name:
            for data in datas:
                movies_name.append(data)

        # 进行电影类型的数据清洗
        for types_data in movie_type:
            type_str = types_data[1].replace('\n', '').replace('／', ' ').strip()
            type_datas.append(type_str)

        # # 进行上映时间的数据清洗
        for date_data2 in movie_date:
            date_str = date_data2[1].replace('\n', '').strip()
            date_datas.append(date_str)

        movies_info = [movies_name, type_datas, date_datas]

        # 将movies_info转为DataFrame
        movies_info_df = pd.DataFrame(movies_info)

        # 转置并拷贝到新的DataFrame
        df_movie_info_res = movies_info_df.T.copy()
        # # 设置列名，写入CSV
        df_movie_info_res.to_csv('../../scrapy_maoyanSpider.csv', index=False, encoding='UTF-8', header=['电影名称', '电影类型', '上映时间'])
        return df_movie_info_res
