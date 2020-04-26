# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 16:13:20 2020

@author: Logvinok-DA
"""

#import requests
from bs4 import BeautifulSoup as bs
#import re
#import pandas as pd
from parsefile import getContent
#
URL = 'https://www.avito.ru/moskva?q=xbox+one+s'

#r = getContent(URL)

xbox = []

for i in range(1,8)[:1]:
    print(i)
    r = getContent(URL + '&p=' + str(i))
#    r = requests.get(URL + '&p=' + str(i), headers={'User-Agent': ua.random})
    items = bs(r.text,'lxml').find_all('div', attrs={'class':'snippet-horizontal'})
    #--#
    for item in items[:2]:
        box = []
        #link
        try:
            link = item.find('a')['href']
        except:
            link=''
        # Наименование объявления
        try:
            name = item.find('a', attrs={'class':'snippet-link'}).text
        except:
            name=''
        # стоимость
        try:
            cost = item.find('span', attrs={'class':'snippet-price'}).text.strip().replace(' ', '').replace('₽','')
        except:
            cost=''
        # Дата публикации
        try:
            date = item.find('div', attrs={'class':'snippet-date-info'}).text.strip()
        except:
            date=''
        
        onepage = 'https://www.avito.ru' + str(link)
        
        page = getContent(onepage)
        
        # Автор объявления
        try:
            author = bs(r.text, 'lxml').find('div', attrs={'class':'seller-info-name js-seller-info-name'}).text.strip()
        except:
            author = ''
        
        try:
            reviews = bs(r.text, 'lxml').find('span', attrs={'class':'seller-info-rating-caption'}).text.strip()
        except:
            reviews = ''
        
        try:
            seller_info = bs(r.text, 'lxml').find_all('div', attrs={'class':'seller-info-value'})[1].div.text.strip()
        
#        заполняем атрибуты по одному объявлению
        box.append(name)
        box.append(cost)
        box.append(date)
        xbox.append(box)