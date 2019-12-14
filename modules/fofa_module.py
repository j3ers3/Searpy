#!/usr/bin/env python
# encoding:utf8
import sys
from util.header import Header
from util.config import *
import base64
import requests
import json

class Fofa:
    def __init__(self, query, page):
        self.query = query
        self.page = page
        self.email = fofa_email
        self.api_key = fofa_key
        self.result = None

    def login(self):
        if not self.api_key:
            print('Automatic authorization failed')
            self.email = raw_input('Email > ').strip()
            self.api_key = raw_input('API KEY > ').strip()


    def search(self):
        query = base64.b64encode(self.query)
        res = []

        try:
            for p in range(1, self.page+1):
                
                url = "https://fofa.so/api/v1/search/all?email={0}&key={1}&qbase64={2}&page={3}".format(self.email, self.api_key, query, p)

                r = requests.get(url, headers=Header.headers, timeout=40)
            
                result_json = json.loads(r.text)
            
                if result_json.get('results'):
                    for item in result_json.get('results'):
                        url = item[0] if '://' in item[0] else 'http://' + item[0]
                        res.append(url)
            self.result = res
        except Exception as e:
            pass





