#!/usr/bin/env python
# encoding:utf8
from util.header import Header
from urllib import quote
import requests
from bs4 import BeautifulSoup

class So:
    def __init__(self, query, page):
        self.query = query
        self.page = page
        self.result = None

    def search(self):
        res = []

        try:
            for p in range(1, self.page+1):
                base_url = 'https://www.so.com/s?q=' + str(quote(self.query)) + '&pn=' + str(p) + '&fr=so.com'

                r = requests.get(base_url, headers=Header.headers, verify=False, timeout=10)
                soup = BeautifulSoup(r.content, "html.parser")
                
                for a in soup.select('li.res-list > h3 > a'):
                    rr = requests.get(a['href'], headers=Header.headers,allow_redirects=True, timeout=5)
                    res.append(rr.url)
                    
            self.result = res
        except Exception as e:
            pass


