# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 16:14:02 2020

@author: Logvinok-DA
"""

import requests
from lxml.html import fromstring
from itertools import cycle
from bs4 import BeautifulSoup as bs
import re

def getProxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr'):
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    proxy_pool = cycle(proxies)
    return {'plen' : len(proxies),
            'proxy_pool': proxy_pool}
    
#####################

#from fake_useragent import UserAgent

def getHeaders():
#    ua = UserAgent()
    headers = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
            'Cache-Control':'max-age=0',
            'Connection':'keep-alive',
            'Host':'www.avito.ru',
            'Referer':'https://www.avito.ru/moskva?q=xbox+one+s',
            'TE':'Trailers',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Chrome'
            }
    return headers

#####################

def getContent(url):
    getp = getProxies()
    try:
        response = requests.get(url, headers = getHeaders())
        if response.status_code == 200:
#            print(response.status_code)
#            print(url)
            if bs(response.text, 'lxml').find('title').text == 'Доступ временно заблокирован':
#                print(bs(response.text, 'lxml').find('title').text)
#                return response
#        else:
                for i in range(int(getp['plen'])):
                    try:
                        proxy_pool = getp['proxy_pool']
                        proxy = next(proxy_pool)
                        print('Try connect {} with proxy {}'.format(i, proxy))
                        response = requests.get(url,proxies={"http": proxy, "https": proxy}, headers = getHeaders())
                        if response.status_code == 200:
                                if bs(response.text, 'lxml').find('title').text != 'Доступ временно заблокирован':
                                    return response
                    except:
                        response = 'err'
        elif response.status_code != 200:
            for i in range(int(getp['plen'])):
                    try:
                        proxy_pool = getp['proxy_pool']
                        proxy = next(proxy_pool)
                        print('Try connect {} with proxy {}'.format(i, proxy))
                        response = requests.get(url,proxies={"http": proxy, "https": proxy}, headers = getHeaders())
                        if response.status_code == 200:
                                if bs(response.text, 'lxml').find('title').text != 'Доступ временно заблокирован':
                                    return response
                    except:
                        response = 'err'
        else:
            return response
        
    except Exception as e:
        print(e)
        
    return response

###################
def maxpage(r):
    pages = [int(x.text) for x in (bs(r.text, 'lxml').find_all('span', attrs={'class':'pagination-item-1WyVp'})) if re.search('\d+',x.text)]
    return max(pages)