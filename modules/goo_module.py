#!/usr/bin/env python
# encoding:utf8
from util.header import Header
from util.config import *
from urllib import quote
import requests
from bs4 import BeautifulSoup

# 被墙，需要代理
class Goo:
    def __init__(self, query, page):
        self.query = query
        self.page = page
        self.result = None
        self.proxy = proxy

    def search(self):
        res = []

        try:
            for p in range(0, self.page*10, 10):
                base_url = 'https://search.goo.ne.jp/web.jsp?MT=' + str(quote(self.query)) + '&FR=' + str(p)

                r = requests.get(base_url, headers=Header.headers, timeout=12, verify=False, proxies=self.proxy)
                soup = BeautifulSoup(r.text, "html.parser")
                
                for a in soup.select('div.result > p.title.fsL1 > a'):
                    res.append(a['href'])
            self.result = res
        except Exception as e:
            #print(e)
            pass
