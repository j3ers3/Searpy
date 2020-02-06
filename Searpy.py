#!/usr/bin/env python3
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
from modules.zoomeye_module import Zoomeye
from modules.yahoo_module import Yahoo

"""
>>> from Searpy import Bing
>>> s = Bing('inurl:php?id=1', 2)
>>> s.search()
>>> for i in s.result:
>>>     print(i)
"""

##########################################################

__version__ = "2.1"
__prog__ = "Searpy"
__author__ = "whois"
__create_date__ = "2016 01 01"
__update_date__ = "2020 01 14"

##########################################################


banner = blue + """
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
 ____
/ ___|  ___  __ _ _ __ _ __  _   _
\___ \ / _ \/ _` | '__| '_ \| | | |
 ___) |  __/ (_| | |  | |_) | |_| |
|____/ \___|\__,_|_|  | .__/ \__, |
                      |_|    |___/\n""" + purple2 + """

                             Searpy Ver. {0}
                             Update {1}
                             Coded by {2}\n""".format(__version__, __update_date__, __author__) + blue + """
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
        usage='Searpy --fofa -s "app=jboss" -p1',
        description="Searpy Engine Tookit",
    )

    engine = parser.add_argument_group('ENGINE')

    engine.add_argument("--baidu", dest="baidu", action="store_true",
                        help="Using baidu Engine")
    engine.add_argument("--google", dest="google", action="store_true",
                        help="Using google Engine")
    engine.add_argument("--so", dest="so", action="store_true",
                        help="Using 360so Engine")
    engine.add_argument("--bing", dest="bing", action="store_true",
                        help="Using bing Engine")
    engine.add_argument("--shodan", dest="shodan", action="store_true",
                        help="Using shodan get favicon")
    engine.add_argument("--fofa", dest="fofa", action="store_true",
                        help="Using fofa Engine")
    engine.add_argument("--zoomeye", dest="zoomeye", action='store_true',
                        help="Using zoomeye Engine")
    engine.add_argument("--goo", dest="goo", action="store_true",
                        help="Using goo Engine")
    engine.add_argument("--yahoo", dest="yahoo", action='store_true',
                        help="Using yahoo Engine")

    script = parser.add_argument_group('SCRIPT')

    script.add_argument("--shodan_ico",
                        help="Get ip list which using the same favicon.ico")

    misc = parser.add_argument_group('MISC')

    misc.add_argument("-s", dest="search",
                      help="Speciy Keyword")
    misc.add_argument("-o", dest="output",
                      help="Specify output file default output.txt")
    misc.add_argument("-p", dest="page", default=1, type=int,
                      help="Search page (default 1)")
    misc.add_argument("-l", dest="limit", default=10, type=int,
                      help="Maximum searching results (default:10) Only Shodan")

    args = parser.parse_args()

    if args.search is None and args.shodan_ico is None:
        print(red + "[x] Searpy -h" + end)
        exit(0)

    if args.zoomeye:
        s = Zoomeye(args.search, args.page)
        s.search()
        for i in s.result:
            save(args.output, i) if args.output else p(i)

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

    if args.yahoo:
        s = Yahoo(args.search, args.page)
        s.search()
        for i in s.result:
            save(args.output, i) if args.output else p(i)

    if args.shodan_ico:
        s = Shodanico(args.shodan_ico)
        s.search(s.get_hash())
