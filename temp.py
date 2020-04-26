# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 16:46:50 2020

@author: Logvinok-DA
"""
import requests
from lxml.html import fromstring
from itertools import cycle
from bs4 import BeautifulSoup as bs
from parsefile import getProxies,getHeaders

url = 'https://www.avito.ru/moskva/igry_pristavki_i_programmy/xbox_one_s_1889635317'

getp = getProxies()

def f(url):
    try:
        response = requests.get(url, headers = getHeaders())
        if response.status_code == 200:
            if bs(response.text, 'lxml').find('title').text == 'Доступ временно заблокирован':
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
        elif response.status_code == 403:
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

r = f(url)

