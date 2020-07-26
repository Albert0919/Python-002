#!/usr/bin/env python
# -*- coding:utf8 -*-
import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.error import URLError, HTTPError


# 设定URL和浏览器headers
url = 'https://maoyan.com/films?showType=3'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
           'Cookie': '__mta=213695019.1595487495390.1595499188968.1595500332357.3; uuid_n_v=v1; \
           uuid=EDEA1480CCB111EABD387F49F1B53159048C14711991467F9E17E122C6774E76; _csrf=44094a4c2463bdced60de161bcfda9200ae9a7abb98d2363f2b54dc2bec746e4; mojo-uuid=afb27aab37e8cc9107c04d016f87635a; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1595487495; _lxsdk_cuid=1737a77246534-07c686f0e4ffec-b7a1334-4b9600-1737a772466c8; _lxsdk=EDEA1480CCB111EABD387F49F1B53159048C14711991467F9E17E122C6774E76; mojo-session-id={"id":"03e1e74c8ca5d44ff4daeb36c01ae512","time":1595498920456}; __mta=213695019.1595487495390.1595487495390.1595499188968.2; mojo-trace-id=5; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1595500332; _lxsdk_s=1737b2579ba-60f-e70-5fd%7C%7C6'}

# 如果出现HTTP或URL错误，则抛出异常
try:
    # 请求地址
    html = requests.get(url, headers=headers)
except HTTPError as e:
    print('错误代码' + e.code)
except URLError:
    print('没有找到此URL')


# 定义详请页面爬虫方法，url:详情页面的url, headers:浏览器的user-agent和cookie
def detail_info(url, headers):
    try:
        detail_html = requests.get(url, headers=headers)
        bs = BeautifulSoup(detail_html.text, 'html.parser')
    except HTTPError:
        print('错误代码' + e.code)
    except URLError:
        print('没有找到此URL')
    # 获取电影名称
    movie_name = bs.find('h1', attrs={'class': 'name'}).text
    # 获取电影类型
    movie_type = bs.find('li', attrs={'class': 'ellipsis'}).text.replace('\n', '')
    # 获取上映时间
    movie_date = bs.find('li', attrs={'class': 'ellipsis'}).find_next_sibling().find_next_sibling().text
    # 返回列表
    return [movie_name, movie_type, movie_date]


# 使用BeautifulSoup进行解析，获取bs对象
bs = BeautifulSoup(html.text, 'html.parser')
# 找到所有div标签，属性为class=movie-item
# 定义空列表，将方法返回值添加至列表中
movie_list = []
# 定义计数器，用于爬取前10个
count = 1

# 找到电影页，获取详情链接
for tags in bs.find_all('div', attrs={'class': 'channel-detail'}):
    if count <= 10:
        for a_tags in tags.find_all('a'):
            # 获取电影信息并添加至列表中，因URL是相对路径，加前导域名
            movie_info = detail_info('https://maoyan.com' + a_tags.get('href'), headers)
            movie_list.append(movie_info)
            count += 1
    else:
        break

# 使用DataFrame转换数据，并写入到CSV中
movie_df = pd.DataFrame(movie_list, columns=['电影名称', '电影类型', '上映时间'])
movie_df.to_csv('./movie_info_requests.csv', encoding='UTF-8', index=False)
