#!/usr/bin/env python
# encoding:utf8
from util.header import Header
import requests
from config import *
from bs4 import BeautifulSoup

class Yahoo:
    def __init__(self, query, page, proxy):
        self.query = query
        self.page = page
        self.result = None
        self.proxy = proxy

    def search(self):
        res = []
        print("[+] Using Yahoo Engine")

        try:
            for p in range(1, (self.page * 10) + 1, 10):
                base_url = 'https://search.yahoo.co.jp/search?p=' + str(self.query) + '&b=' + str(p)

                r = requests.get(base_url, headers=Header.bing_headers, cookies=Header.cookies, verify=False,
                                 timeout=15, proxies=self.proxy)

                soup = BeautifulSoup(r.content, "html.parser")
                
                for n in range(1, 11):
                    for a in soup.select('#contents__wrap > div.Contents__inner.Contents__inner--main > div.Contents__innerGroupBody > div:nth-child({}) > div > section > div.sw-Card__section.sw-Card__section--header > div > div > a'.format(n)):
                        res.append(a['href'])

            if res is None:
                print("[x] Not result !!!")
                exit(1)
            self.result = res 

        except Exception as e:
            print("[x] Network is error !!!")
            exit(1)
