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
from modules.quake_module import Quake
from modules.hunter_module import Hunter

"""
>>> from Searpy import Bing
>>> s = Bing('inurl:php?id=1', 2)
>>> s.search()
>>> for i in s.result:
>>>     print(i)
"""

##########################################################

__version__ = "2.4"
__prog__ = "Searpy"
__author__ = "nul1"
__create_date__ = "2016 01 01"
__update_date__ = "2022 07 11"

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


# 子域名发现模块
def subdomain(domain):
    fofa_search = 'host="{}"'.format(domain)
    search = 'site:{} -www'.format(domain)
    output = '{}.txt'.format(domain)

    fofa = Fofa(fofa_search, 10, output)
    fofa.login()
    fofa.search()
    print("[+] Fofa done")

    shodan = Shodan(domain, None)
    shodan.login()
    shodan.subdomain()
    for i in shodan.result:
        save(output, i)
    print("[+] Shodan done")

    bing = Bing(search, 15)
    bing.search()
    for i in bing.result:
        save(output, i)
    print("[+] Bing done")


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
                        help="Using shodan Engine")
    engine.add_argument("--fofa", dest="fofa", action="store_true",
                        help="Using fofa Engine")
    engine.add_argument("--zoomeye", dest="zoomeye", action='store_true',
                        help="Using zoomeye Engine")
    engine.add_argument("--goo", dest="goo", action="store_true",
                        help="Using goo Engine")
    engine.add_argument("--yahoo", dest="yahoo", action='store_true',
                        help="Using yahoo Engine")
    engine.add_argument("--quake", dest="quake", action='store_true',
                        help="Using quake Engine")
    engine.add_argument("--hunter", dest="hunter", action='store_true',
                        help="Using hunter Engine")


    script = parser.add_argument_group('SCRIPT')

    script.add_argument("--shodan_icon",
                        help="Get ip list which using the same favicon.ico")
    script.add_argument("--fofa_icon",
                        help="Get ip list which using the same favicon.ico")
    script.add_argument("--subdomain",
                        help="Get subdomain")

    misc = parser.add_argument_group('MISC')

    misc.add_argument("-s", dest="search",
                      help="Speciy Keyword")
    misc.add_argument("-o", dest="output",
                      help="Specify output file default output.txt")
    misc.add_argument("-p", dest="page", default=1, type=int,
                      help="Search page (default 1)")
    misc.add_argument("-l", dest="limit", default=10, type=int,
                      help="Maximum searching results (default:10) Only Shodan")
    misc.add_argument("--proxy", dest="proxy", help="HTTP Proxy, eg http://127.0.0.1:8080")

    args = parser.parse_args()

    if args.search is None and args.shodan_icon is None and args.fofa_icon is None and args.subdomain is None:
        parser.print_help()

    proxies = {"http": args.proxy, "https": args.proxy} if args.proxy else {}

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
        s = Fofa(args.search, args.page, args.output, proxies)
        s.login()
        s.search()

    if args.baidu:
        s = Baidu(args.search, args.page, proxies)
        s.search()
        for i in s.result:
            save(args.output, i) if args.output else p(i)

    if args.bing:
        s = Bing(args.search, args.page, proxies)
        s.search()
        for i in s.result:
            save(args.output, i) if args.output else p(i)

    if args.google:
        s = Google(args.search, args.page, proxies)
        s.search()
        for i in s.result:
            save(args.output, i) if args.output else p(i)

    if args.so:
        s = So(args.search, args.page, proxies)
        s.search()
        for i in s.result:
            save(args.output, i) if args.output else p(i)

    if args.goo:
        s = Goo(args.search, args.page, proxies)
        s.search()
        for i in s.result:
            save(args.output, i) if args.output else p(i)

    if args.yahoo:
        s = Yahoo(args.search, args.page, proxies)
        s.search()
        for i in s.result:
            save(args.output, i) if args.output else p(i)

    if args.quake:
        s = Quake(args.search, args.page, args.output, proxies)
        s.login()
        s.search()

    if args.hunter:
        s = Hunter(args.search, args.page, args.output, proxies)
        s.login()
        s.search()

    if args.shodan_icon:
        s = Shodanico(args.shodan_icon)
        s.search(s.get_hash())

    if args.fofa_icon:
        i_hash = Shodanico(args.fofa_icon).get_hash()
        search = 'icon_hash="{}"'.format(i_hash)
        s = Fofa(search, args.page, args.output)
        s.login()
        s.search()

    if args.subdomain:
        subdomain(args.subdomain)
