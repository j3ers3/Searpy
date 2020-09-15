#!/usr/bin/env python
# encoding:utf8
import requests
import json
from util.header import Header
from config import *

class Zoomeye:
    def __init__(self, query, page):
        self.query = query
        self.page = page
        self.web_url = 'https://api.zoomeye.org/web/search'
        self.host_url = 'https://api.zoomeye.org/host/search'
        self.user = zoomeye_email
        self.pwd = zoomeye_password
        self.result = None

    def login(self):
        login_url = 'https://api.zoomeye.org/user/login'
        data = {'username': self.user, 'password': self.pwd}
        r = requests.post(url=login_url, json=data)
        if r.status_code != 200:
            print("[x] Login False")
            exit(1)
        print("[+] Get access_token")
        token = r.json().get('access_token')
        return token

    # web搜索
    def search(self):
        print("[+] Using Zoomeye Engine")

        res = []
        access_token = self.login()

        header = Header.headers
        header.update({'Authorization': 'JWT ' + access_token})

        try:

            for p in range(1, self.page + 1):
                params = {'query': self.query, 'page': self.page}
                r = requests.get(self.web_url, headers=header, data=params, verify=False)
                result_json = json.loads(r.text)
                if result_json.get('matches'):
                    # print("[+] Total {0}".format(result_json.get('total')))
                    for item in result_json.get('matches'):
                        ip = item['ip'][0]
                        res.append(ip)
                else:
                    break

            if res is None:
                print("[x] Not result !!!")
                exit(1)
            self.result = res

        except Exception as e:
            print(e)

