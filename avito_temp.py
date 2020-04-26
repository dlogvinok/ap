# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 13:54:33 2020

@author: Logvinok-DA
"""

import requests
from bs4 import BeautifulSoup as bs

URL = 'https://www.avito.ru/moskva/igry_pristavki_i_programmy/konsol_xbox_one_s_1tb_novyy_traid_in_opt_1844192698'
#

for i in range(len(proxies)):
    proxy = next(proxy_pool)
    print('Request #' + str(i) +' proxy ' + str(proxy))
    try:
        response = requests.get(URL,proxies={"http": proxy, "https": proxy}, headers=headers)
        if response.status_code == 200:
            if bs(response.text, 'lxml').find('title').text != 'Доступ временно заблокирован':
                print('Get it. Done')
                break
    except:
        print("Skipping. Connnection error")
        

#url = 'https://httpbin.org/ip'
#for i in range(1,11):
#    #Get a proxy from the pool
#    proxy = next(proxy_pool)
#    print("Request #%d"%i)
#    try:
#        response = requests.get(url,proxies={"http": proxy, "https": proxy})
#        print(response.json())
#    except:
#        #Most free proxies will often get connection errors. You will have retry the entire request using another proxy to work. 
#        #We will just skip retries as its beyond the scope of this tutorial and we are only downloading a single url 
#        print("Skipping. Connnection error")

#ua = UserAgent()
#URL = 'https://www.avito.ru/moskva/igry_pristavki_i_programmy/konsol_xbox_one_s_1tb_novyy_traid_in_opt_1844192698'
#
#def save_image(name, file_object):
#    with open(name, 'bw') as f:
#        for chunk in file_object.iter_content(8192):
#            f.write(chunk)
#
#headers = {
#        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#        'Accept-Encoding':'gzip, deflate, br',
#        'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
#        'Cache-Control':'max-age=0',
#        'Connection':'keep-alive',
#        'Host':'www.avito.ru',
#        'Referer':'https://www.avito.ru/moskva?q=xbox+one+s',
#        'TE':'Trailers',
#        'Upgrade-Insecure-Requests':'1',
#        'User-Agent':ua.random
#        }