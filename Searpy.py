#!/usr/bin/env python
# encoding:utf8
import argparse
from util.color import *
from modules.shodan_module import Shodan
from modules.fofa_module import Fofa
from modules.baidu_module import Baidu
from modules.bing_module import Bing
from modules.google_module import Google
from modules.so_module import So
from modules.goo_module import Goo
from modules.shodanico_module import Shodanico
"""
>>> from Searpy import Bing
>>> s = Bing('inurl:php?id=1', 2)
>>> s.search()
>>> for i in s.result:
>>>     print(i)
"""

##########################################################

__version__ = "2.0"
__prog__    = "Searpy"
__author__  = "whois"
__create_date__  = "2016/01/01"

##########################################################


banner = blue + """
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
 ____
/ ___|  ___  __ _ _ __ _ __  _   _
\___ \ / _ \/ _` | '__| '_ \| | | |
 ___) |  __/ (_| | |  | |_) | |_| |
|____/ \___|\__,_|_|  | .__/ \__, |
                      |_|    |___/\n""" + purple2 + """

                             Searpy Ver. 2.0
                             Update 2019 12 11
                             Coded by whois\n""" + blue + """
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n""" + end



def save(save_file, content):
    with open(save_file, 'a') as f:
        try:
            f.writelines(content + '\n')
        except Exception as e:
            pass

def p(i):
    print(yellow + i + end)


if __name__ == '__main__':
    print(banner)
    parser = argparse.ArgumentParser(
        description="Searpy Engine Tookit", 
        version="{0}: {1} ({1})".format(__prog__, __version__, __author__),
        epilog='''Example: 
            Searpy --shodan_ico sec-wiki.com''')

    parser.add_argument("--baidu", dest="baidu", action="store_true",
                        help="Using baidu Engine")
    parser.add_argument("--google", dest="google", action="store_true",
                        help="Using google Engine")
    parser.add_argument("--so", dest="so", action="store_true",
                        help="Using 360so Engine")
    parser.add_argument("--bing", dest="bing", action="store_true",
                        help="Using bing Engine")
    parser.add_argument("--shodan", dest="shodan", action="store_true",
                        help="Using shodan get favicon")
    parser.add_argument("--fofa", dest="fofa", action="store_true",
                        help="Using fofa Engine")
    parser.add_argument("--zoomeye", dest="zoomeye", action='store_true', 
                        help="Using zoomeye Engine")
    parser.add_argument("--goo", dest="goo", action="store_true",
                        help="Using goo Engine")

    parser.add_argument("--shodan_ico",
                        help="Get ip list which using the same favicon.ico")
    parser.add_argument("-s", dest="search", 
                        help="Speciy Keyword")
    parser.add_argument("-o", dest="output", 
                        help="Specify output file default output.txt")
    parser.add_argument("-p", dest="page",default=1, type=int, 
                        help="Search page (default 1)")
    parser.add_argument("-l", dest="limit", default=10, type=int, 
                        help="Maximum searching results (default:10) Only Shodan")

    args = parser.parse_args()

    if args.search == None and args.shodan_ico == None:
        print(red + "[x] Searpy -h" + end)
        exit(0)

    if args.zoomeye:
        pass

    if args.shodan:
        s = Shodan(args.search, args.limit)
        s.login()
        s.info()
        s.search()
        for i in s.result:
            save(args.output, i) if args.output else p(i)

    if args.fofa:
        s = Fofa(args.search, args.page)
        s.login()
        s.search()
        for i in s.result:
            save(args.output, i) if args.output else p(i)
            
    if args.baidu:
        s = Baidu(args.search, args.page)
        s.search()
        for i in s.result:
            save(args.output, i) if args.output else p(i)

    if args.bing:
        s = Bing(args.search, args.page)
        s.search()
        for i in s.result:
            save(args.output, i) if args.output else p(i)

    if args.google:
        s = Google(args.search, args.page)
        s.search()
        for i in s.result:
            save(args.output, i) if args.output else p(i)

    if args.so:
        s = So(args.search, args.page)
        s.search()
        for i in s.result:
            save(args.output, i) if args.output else p(i)

    if args.goo:
        s = Goo(args.search, args.page)
        s.search()
        for i in s.result:
            save(args.output, i) if args.output else p(i)

    if args.shodan_ico:
        s = Shodanico(args.shodan_ico)
        s.search(s.get_hash())
   
