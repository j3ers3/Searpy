#!/usr/bin/env python
# encoding:utf8
from util.header import Header
from urllib import quote
import requests
from bs4 import BeautifulSoup

class Bing:
    def __init__(self, query, page):
        self.query = query
        self.page = page
        self.result = None

    def search(self):
        res = []

        try:
            for p in range(1, (self.page*10)+1, 10):
                base_url = 'https://cn.bing.com/search?q=' + str(quote(self.query)) + '&first=' + str(p)
                #print base_url
                r = requests.get(base_url, headers=Header.bing_headers, cookies=Header.cookies, verify=False, timeout=15)
                soup = BeautifulSoup(r.content, "html.parser")
                #print(soup)
                
                # 先查找id=b_results -> 子标签类b_algo -> 查找标签<h2> -> 查找标签<a> -> 获取href
                for a in soup.select('#b_results > .b_algo > h2 > a'):
                    #print a
                    res.append(a['href'])
            self.result = res
        except Exception as e:
            pass