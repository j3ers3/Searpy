#!/usr/bin/env python3
# encoding:utf8
from util.header import Header
from config import *
import base64
import requests
import json


class Hunter:
    def __init__(self, query, page, output, proxy):
        self.query = query
        self.page = page
        self.api_key = hunter_key
        self.result = None
        self.output = output
        self.proxy = proxy

    def login(self):
        if not self.api_key:
            print('Automatic authorization failed')
            self.email = input('Email > ').strip()
            self.api_key = input('API KEY > ').strip()

    def search(self):
        query = base64.urlsafe_b64encode(self.query.encode("utf-8")).decode('utf-8')
        res = []
        print("[*] Using Hunter Engine")

        try:
            for p in range(1, self.page + 1):

                url = "https://hunter.qianxin.com/openApi/search?api-key={}&search={}&page={}&page_size=10&is_web=1".format(self.api_key, query, p)

                r = requests.get(url, headers=Header.headers, timeout=15, verify=False, proxies=self.proxy)

                result_json = json.loads(r.text)

                if result_json.get('data'):
                    for item in result_json['data']['arr']:
                        print(item['url'])
                        res.append(item['url'])
                  
                        if self.output:
                            with open(self.output, 'a') as f:
                                f.writelines(url + '\n')       
                else:
                    print(result_json)
                    break

        except Exception as e:
            print(e)
            pass
