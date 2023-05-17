#!/usr/bin/env python
# encoding:utf8
from util.header import Header
import requests
from bs4 import BeautifulSoup


class Bing:
    def __init__(self, query, page, proxy):
        self.query = query
        self.page = page
        self.result = None
        self.proxy = proxy

    def search(self):
        res = []
        print("[*] Using Bing Engine")

        try:
            for p in range(1, (self.page * 10) + 1, 10):
                base_url = 'https://cn.bing.com/search?q=' + str(self.query) + '&first=' + str(p)
           
                r = requests.get(base_url, headers=Header.bing_headers, cookies=Header.cookies, verify=False,
                                 timeout=15, proxies=self.proxy)
                soup = BeautifulSoup(r.content, "html.parser")

                for a in soup.select('#b_results > .b_algo > .b_title > a'):
                    res.append(a['href'])

            if res is None:
                print("[x] Not result !!!")
                exit(1)
            self.result = res

        except Exception as e:
            print("[x] Network is error !!!")
            exit(1)
