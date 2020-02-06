#!/usr/bin/env python
# encoding:utf8
import shodan
import sys
from shodan.exception import APIError
from util.config import *

class Shodan:
    def __init__(self, query, limit):
        self.query = query
        self.limit = limit
        self.api_key = shodan_key
        self.result = None

    def login(self):
        if not self.api_key:
            print('Automatic authorization failed')
            self.api_key = raw_input('API KEY > ').strip()

    def info(self):
        try:
            api = shodan.Shodan(self.api_key)
            account_info = api.info()
            search_count = api.count(self.query)['total']
            print("[+] Available Shodan query credits: {0}").format(account_info.get('query_credits'))
            print("[+] {0} count {1}".format(self.query, search_count))
            print('')
        except APIError as e:
            sys.exit(e)
        return True

    def search(self):
        print("[+] Using Shodan Engine")

        try:
            api = shodan.Shodan(self.api_key)
            result = api.search(query=self.query, limit=self.limit)
        except APIError as e:
            sys.exit(e)

        if 'matches' in result:
            res = []
            for match in result.get('matches'):
                res.append(match.get('ip_str') + ':' + str(match.get('port')))
            self.result = res
            
        else:
            self.result = []

