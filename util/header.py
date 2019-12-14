from random import choice

class Header:
    
    agents_list = ['Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',
                'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240',
            ]

    headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
                'Accept-Charset':'GB2312,utf-8;q=0.7,*;q=0.7', 
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate, sdch, br',
                'Cache-Control':'max-age=0', 
                'Connection':'keep-alive', 
                'Referer': 'https://www.baidu.com',
                'Cookie': '__jsluid=fae27ad046bd22fca181a42209bf2a21;',
                'User-Agent': choice(agents_list), 
            }



    bing_headers = {"Connection": "close", "Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36", "Sec-Fetch-User": "?1", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3", "Sec-Fetch-Site": "none", "Sec-Fetch-Mode": "navigate", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7", "x-forwarded-for": "127.0.0.1"}


    cookies = {"SRCHD": "AF=NOFORM", "SRCHUID": "V=2&GUID=04B0C23741984D93A7869B242C5A7B9D&dmnchg=1", "ULC": "P=1D8BA|1:1&H=1D8BA|1:1&T=1D8BA|1:1", "ENSEARCH": "TIPBUBBLE=1&BENVER=0", "MUID": "2AF5F552F59C66673A52F88BF19C650F", "MUIDB": "2AF5F552F59C66673A52F88BF19C650F", "_EDGE_S": "mkt=zh-cn&SID=355C60C46D5F66EF20C76EF46C71671B", "OID": "AhAf0PJ6XP_zDuQ8dzSyzi0UP2hDl--yLGMTsCz5Opbun2_JEiOtdGkFLnuzrtDv74VB2E1gAgXe5C_tQ8kCjL4k", "OIDI": "AhAFLOwJu7qJJl9MvUAx9gG83gl15hS16xcNxo8KaN84ug", "ipv6": "hit=1576211234886&t=4", "SRCHUSR": "DOB=20191113&T=1576317051000", "SRCHHPGUSR": "CW=1440&CH=433&DPR=2&UTC=480&WTS=63711913851", "_SS": "SID=355C60C46D5F66EF20C76EF46C71671B&bIm=961168&HV=1576317803"}
    
    headers = {"Connection": "close", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36", "Sec-Fetch-User": "?1", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Referer": "https://cn.bing.com/search?q=aaa&qs=n&form=QBRE&sp=-1&pq=aaa&sc=0-14&sk=&cvid=754946128E844B0D97686720A073DBDC", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7", "x-forwarded-for": "118.11.11.1"}



