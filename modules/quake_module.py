#!/usr/bin/env python3
# encoding:utf8
from config import *
import requests
import json


class Quake:
    def __init__(self, query, page, output, proxy):
        self.query = query
        self.page = page
        self.api_key = quake_key
        self.result = None
        self.output = output
        self.proxy = proxy

    def login(self):
        if not self.api_key:
            print('Automatic authorization failed')
            self.api_key = input('API KEY > ').strip()

    def search(self):
        res = []
        print("[+] Using 360 quake Engine")
        headers = {
            "X-QuakeToken": self.api_key,
            "Content-Type": "application/json",
        }

        try:
            for p in range(1, self.page + 1):
                url = "https://quake.360.cn/api/v3/search/quake_service"
                data = {
                    "query": "{0}".format(self.query),
                    "start": p,
                    "size": 15,
                    "ignore_cache": False,
                }
                r = requests.post(url, headers=headers, json=data, timeout=15, verify=False, proxies=self.proxy)
                result_json = json.loads(r.text)
                
                if result_json.get('data'):
                    for item in result_json.get('data'):
                        s = item.get('service')
                        h = s.get('http')
                        url = h['host'] if '://' in h['host'] else 'http://' + h['host'] + ':' + str(item['port'])
      
                        print(url)
                        if self.output:
                            with open(self.output, 'a') as f:
                                f.writelines(url + '\n')            
                else:
                    break
        except Exception as e:
            print(e)
            pass
