#!/usr/bin/env python
# encoding:utf8

from urllib import quote
import requests
from util.config import *
from util.header import Header
from bs4 import BeautifulSoup
from time import sleep

class Google:
    def __init__(self, query, page):
        self.query = query
        self.page = page
        self.result = None
        self.proxy = proxy

    def search(self):
        res = []

        try:
            for p in range(0, (self.page*10), 10):
                base_url = 'https://www.google.com/search?safe=strict&q=' + str(quote(self.query)) + '&oq=' + str(quote(self.query)) + 'start=' + str(p)

                r = requests.get(base_url, headers=Header.bing_headers, verify=False, timeout=14, proxies=self.proxy)
                soup = BeautifulSoup(r.content, "html.parser")
                
                for a in soup.select('div.rc > div.r > a'):
                    url = a['href']
                    if 'translate.google.com' not in url:
                        res.append(url)
                        
                # 防止请求过于频繁导致限制
                sleep(2)
            self.result = res
        except Exception as e:
            pass