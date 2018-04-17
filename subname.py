
# encoding:utf8
from Searpy import bing, baidu, google, so
from urllib2 import urlparse
import sys

if len(sys.argv) < 3:
    print "[x] Usage: python subname.py domain.com [baidu|bing|google|so] page(default 6)"
    print "[x] Example: python subname.py baidu.com google 10"
    exit(1)

domain_list = []
page = 6 if len(sys.argv)==3 else int(sys.argv[3])

def subsearch(domain, engine, page):

    if engine not in ['baidu', 'bing', 'google', 'so']:
        print '[x] Engine: baidu bing google so : ('
        exit(2)

    if engine == 'baidu':
        print '[B] Using Baidu search engines : )'
        url_list = baidu('site:{0}'.format(domain), page)
    if engine == 'bing':
        print '[B] Using Bing search engines : )'
        url_list = bing('site:{0}'.format(domain), page)
    if engine == 'google':
        print '[G] Using Goolge search engines : )'
        url_list = google('site:{0}'.format(domain), page)   
    if engine == 'so':
        print '[3] Using 360 search engines : )'
        url_list = so('site:{0}'.format(domain), page)

    for url in url_list:
        domain = urlparse.urlsplit(url)[1]
        if domain not in domain_list:
            domain_list.append(domain)

    return domain_list


if __name__ == '__main__':
    for d in subsearch(sys.argv[1], sys.argv[2], page):
        print d
    print "\nA total of {0} domains".format(len(domain_list))
    print "\t -->  Happy Hacking : )"
