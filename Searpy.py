#!/usr/bin/env python
# encoding:utf8
import requests
import re
import sys
import optparse
from bs4 import BeautifulSoup
from urllib import quote
from random import choice

"""
    >>> from Searpy import baidu

    >>> b = baidu('powered by discuz', 1)

    >>> for url in b:print url

"""

##########################################################

__version__ = "1.1"
__prog__    = "Searpy"
__author__  = "whois"
__date__  = "2016/01/01"

##########################################################

col_purp = '\033[95m'
col_cyan = '\033[96m'
col_blue = '\033[94m'
col_red = '\033[90m'
col_end  = '\033[0m'


banner = col_blue + """
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
 ____
/ ___|  ___  __ _ _ __ _ __  _   _
\___ \ / _ \/ _` | '__| '_ \| | | |
 ___) |  __/ (_| | |  | |_) | |_| |
|____/ \___|\__,_|_|  | .__/ \__, |
                      |_|    |___/\n""" + col_cyan + """

                             Searpy Ver. 1.1
                             Update 2018 04 17
                             Coded by whois\n""" + col_blue + """
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n""" + col_end


# set shadowsocks proxy
Proxy = {
    'http':'http://127.0.0.1:1080',
    'https':'http://127.0.0.1:1080'
    }

Agents_list = ['Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',
                'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240',
            ]

Headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
                'Accept-Charset':'GB2312,utf-8;q=0.7,*;q=0.7', 
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate, sdch, br',
                'Cache-Control':'max-age=0', 
                'Connection':'keep-alive', 
                'Referer': 'https://www.baidu.com',
                'Cookie': '__jsluid=fae27ad046bd22fca181a42209bf2a21;',
                'User-Agent': choice(Agents_list), 
            }

def save_file(save_file, content):
    with open(save_file, 'a') as f:
        try:
            f.writelines(content + '\n')
        except:
            pass


# 钟馗之眼
def zoomeye(search, page, z_type):

    """
        app:"Drupal" country:"JP"

    """
    #url_login = "https://api.zoomeye.org/user/login"
    url_api = "https://www.zoomeye.org/api/search"

    # 认证信息
    Headers2 = {"Cube-Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6IjI5OTY0Nzk4MjhAcXEuY29tIiwidXVpZCI6Ijk1YWQyZTY2NTk2MjlkNjMyMjZlZjI0MzUyMmQyNDA3IiwiaWF0IjoxNTIzOTQzNjM2LCJleHAiOjE1MjQwMzAwMzZ9.DdGIDsP4NnX_xkpm1IEmvnfYYmZqSl7V20Oc8axY3EE"}

    print col_red + "[!] Using zoomeye with type {0}\n".format(z_type) + col_end

    for n in xrange(1, page+1):
        try:
            data = {'q':search, 'p':str(n), 't':z_type}
            r = requests.get(url_api, params=data, headers=Headers2)
       
            if z_type == 'host':
                result = [str(item['ip'])+':'+str(item['portinfo']['port']) for item in eval(r.content)['matches']]
            elif z_type == 'web':
                rer = re.compile('"url": "(.*?)"')
                result = rer.findall(r.content)
            yield result
        except Exception:
            yield None



# 百度搜索
def baidu(search,page):

    for n in xrange(0, page*10, 10):
        base_url = 'https://www.baidu.com/s?wd=' + str(quote(search)) + '&oq=' + str(quote(search)) + '&ie=utf-8' + '&pn=' + str(n)
        try:
            r = requests.get(base_url, headers=Headers)
            soup = BeautifulSoup(r.text, "html.parser")
            for a in soup.select('div.c-container > h3 > a'):
                url = requests.get(a['href'], headers=Headers, timeout=5).url
                yield url
        except:
            yield None


# 360搜索
def so(search, page):

    for n in xrange(1, page+1):
        base_url = 'https://www.so.com/s?q=' + str(quote(search)) + '&pn=' + str(n) + '&fr=so.com'
        try:
            r = requests.get(base_url, headers=Headers)
            soup = BeautifulSoup(r.text, "html.parser")
            for a in soup.select('li.res-list > h3 > a'):
                url1 = requests.get(a['href'], headers=Headers, timeout=5)
                url = re.findall("URL='(.*?)'", url1.text)[0] if re.findall("URL='(.*?)'", url1.text) else url1.url
                yield url
        except:
            yield None


# 必应搜索
def bing(search, page):

    for n in xrange(1, (page*10)+1, 10):
        base_url = 'http://cn.bing.com/search?q=' + str(quote(search)) + '&first=' + str(n)
        try:
            r = requests.get(base_url, headers=Headers)
            soup = BeautifulSoup(r.text, "html.parser")
            for a in soup.select('li.b_algo > div.b_algoheader > a'):
                url = a['href']
                yield url
        except:
            yield None


# Google搜索
def google(search, page):

    for n in xrange(0, 10*page, 10):
        base_url = 'https://www.google.com.hk/search?safe=strict&q=' + str(quote(search)) + '&oq=' + str(quote(search)) + 'start=' + str(n)
        try:
            r = requests.get(base_url, headers={'User-Agent': choice(Agents_list)}, proxies=Proxy, timeout=16)
            soup = BeautifulSoup(r.text, "html.parser")
            for a in soup.select('div.rc > h3.r > a'):
                url = a['href']
                yield url
        except Exception as e:
            yield None



if __name__ == '__main__':

    print banner
    parser = optparse.OptionParser(
                usage="Usage: %prog [options]",
                version="%s: v%s (%s)" % (__prog__, __version__, __author__),
                epilog="""Example: Searpy --bing -s "inurl:action" -p10 -o file.txt
                          Example: Searpy.py -z -s "app:Drupal" -t host -p10 -o drupal.txt""",
            )

    parser.add_option("-z", "--zoomeye", action='store_true', dest="zoomeye",
            help="Using zoomeye search")
    parser.add_option("-b", "--baidu", action="store_true", dest="baidu",
            help="Using baidu search")
    parser.add_option("-g", "--google", action="store_true", dest="google",
            help="Using google search")
    parser.add_option("-x", "--360so", action="store_true", dest="so",
            help="Using 360so search")
    parser.add_option("-i", "--bing", action="store_true", dest="bing",
            help="Using bing search")
    parser.add_option("-s", "--search", dest="search",type="string",
            help="Specify Keyword")
    parser.add_option("-o", "--output", dest="output",
            type="string", help="Specify output file default output.txt")
    parser.add_option("-t", "--type", dest="type1", default="web",
            type="string", help="Zoomeye Search Type default [web],[host]")
    parser.add_option("-p","--page",dest="page",default=2,
            type="int", help="Search Engine page default 2")

    (options, args) = parser.parse_args()

    if options.zoomeye == None and options.baidu == None and options.so == None and options.google == None and options.bing == None:
        print col_red + "[x] Please use -h to see help" + col_end
        sys.exit(0)

    if options.zoomeye:
        for z in zoomeye(options.search, options.page, options.type1):
            for url in z:
                if options.output:
                    print url
                    save_file(options.output, url)
                else:
                    print url

    if options.baidu:
        for url in baidu(options.search, options.page):
            if options.output:
                print url
                save_file(options.output, url)
            else:
                print url

    if options.so:
        for url in so(options.search, options.page):
            if options.output:
                print url
                save_file(options.output, url)
            else:
                print url

    if options.bing:
        for url in bing(options.search, options.page):
            if options.output:
                print url
                save_file(options.output, url)
            else:
                print url

    if options.google:
        for url in google(options.search, options.page):
            if options.output:
                try:
                    print url
                    save_file(options.output, url)
                except:
                    pass
            else:
                try:
                    print url
                except:
                    pass
