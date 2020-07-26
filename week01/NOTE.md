学习笔记

## 开发的四个步骤
1. 提出需求
2. 编码
3. 代码run
4. 修复bug和完善

## url.request和requests的区别
1. 使用url.request需要read和decode
2. 使用requests调用.get方法即可请求

## BeautifulSoup使用
1. 使用pip install bs4安装相应库
2. 使用from bs4 import BeautifulSoup导入包
3. 生成BeautifulSoup对象，通过.find_all方法查找属性，.text获取相应节点的文本

## Xpath
1. xpath由lxml的etree进行实现，可通过绝对路径、相对路径进行查找
2. Scrapy内的xpath可使用extract()方法进行取值
   
## 爬虫自动翻页功能
1. 将爬虫页面入口的URL传入至新的自定义方法内，使用requests继续请求相应URL
2. 用过URL上的get参数，判断规律，找到page数，用循环进行处理

## HTML和HTTP协议
1. HTML常用标签：span、div、img、a等标签
2. HTTP协议具有header头和Cookie，目的是让服务端知道使用的是浏览器进行的访问

## Scrapy组件
1. Scrapy可使用多个Spider，通过引擎传入后给到调度器，按照先后顺序，去除重复的请求
2. 下载器：用于下载网页内容，并返回给Spider
3. 爬虫需要自己编写逻辑代码，可从页面提取链接，也可以继续抓取下一个页面
4. items负责处理网页抽取的实体，可持久化、验证实体有效性
5. 中间件：通常由Scrapy自行调用

## Scrapy安装与使用
1. 使用pip install scrapy安装
2. 使用scrapy startproject 爬虫名称
3. 切换到相应路径，使用scrapy genspider 域名生成爬虫

## yield的使用
1. yield对应于函数的return关键字，可将值进行返回
2. yield可一个一个的返回值，通常用于迭代器
3. yield可以使用next()、list()进行返回
