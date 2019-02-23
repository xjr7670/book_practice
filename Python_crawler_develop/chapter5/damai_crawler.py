#-*- coding:utf-8 -*-

from lxml import html
import requests


url = 'https://search.damai.cn/search.htm'
res = requests.get(url)
src = res.text

selector = html.fromstring(src, 'lxml')
item_list = selector.xpath('//ul[@id="content_list"]/li')
item_dict_list = []

for item in item_list:
    
