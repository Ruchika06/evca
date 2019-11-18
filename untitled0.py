#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on Fri Nov 15 11:12:49 2019

@author: ruchika
'''

from bs4 import BeautifulSoup
import requests
import csv
from bs4 import BeautifulSoup
html_doc =  open('/home/ruchika/Documents/Deforestation statistics for India.html')
soup = BeautifulSoup(html_doc, 'lxml')
for table in soup.find_all('div', class_='datatable'):
    try:
        print(table.th.text)
        print(table.tr.text)
    except AttributeError:
        pass
    print()
    
'''
csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])


for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']

        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]

        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None

    print(yt_link)

    print()

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()
'''
