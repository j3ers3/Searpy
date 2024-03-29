#!/usr/bin/env python3
# encoding:utf8
from util.header import Header
import requests
from bs4 import BeautifulSoup

class So:
    def __init__(self, query, page, proxy):
        self.query = query
        self.page = page
        self.result = None
        self.proxy = proxy

    def search(self):
        res = []
        print("[+] Using 360SO Engine.")

        try:
            for p in range(1, self.page+1):
                base_url = 'https://www.so.com/s?q=' + str(self.query) + '&pn=' + str(p) + '&fr=so.com'

                r = requests.get(base_url, headers=Header.headers, verify=False, timeout=10, proxies=self.proxy)
                soup = BeautifulSoup(r.content, "html.parser")
                
                for a in soup.select('li.res-list > h3 > a'):
                    url = a['data-mdurl']
                    res.append(url)

            if res is None:
                print("[x] Not result !!!")
                exit(1)
            self.result = res

        except Exception as e:
            print(e)
            print("[x] Network is error !!!")
            exit(1)


