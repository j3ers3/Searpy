#!/usr/bin/env python
# encoding:utf8
from util.header import Header
import requests
from bs4 import BeautifulSoup


class Baidu:
    def __init__(self, query, page):
        self.query = query
        self.page = page
        self.result = None

    def search(self):
        res = []
        print("[+] Using Baidu Engine")

        for p in range(0, self.page * 10, 10):
            base_url = 'https://www.baidu.com/s?wd=' + str(self.query) + '&oq=' + str(
                self.query) + '&ie=utf-8&pn=' + str(p)
            # print(base_url)

            try:
                r = requests.get(base_url, headers=Header.headers, timeout=10, verify=False, allow_redirects=True)
                soup = BeautifulSoup(r.text, "html.parser")

                # 获取跳转链接
                for a in soup.select('div.c-container > h3 > a'):
                    url = requests.get(a['href'], headers=Header.headers, allow_redirects=True, timeout=7,
                                       verify=False).url
                    res.append(url)

                if res is None:
                    print("[x] No result!!")
                    exit(1)
                self.result = res

            except Exception as e:
                print("[x] Network is error !!!")
                exit(1)
