#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 09:58:02 2017

@author: cavin
"""

import re
import csv
from time import sleep
from collections import Counter

import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup


def get_domain(email_address):
    """split on '@' and return the last piece"""
    return email_address.lower().split("@")[-1]

#with open('email_address.txt', 'r') as f:
#    domain_counts = Counter(get_domain(line.strip()) \
#                            for line in f \
#                            if "@" in line)
#    
#with open('tab_delimited_stock_prices.txt', 'rb') as f:
#    reader = csv.reader(f, delimiter="\t")
#    for row in reader:
#        date = row[0]
#        symbol = row[1]
#        closing_price = float(row[2])
#        process(date, symbol, closing_price)
#
#with open('colon_delimited_stock_prices.txt', 'rb') as f:
#    reader = csv.DictReader(f, delimiter=':')
#    for row in reader:
#        date = row['date']
#        symbol = row['symbol']
#        closing_price = float(row['closing_price'])
#        process(date, symbol, closing_price)
#
#today_prices = {'AAPL': 90.91, 'MSFT': 41.68, 'FB': 64.5}
#
#with open('comma_delimited_stock_prices.txt', 'wb') as f:
#    writer = csv.writer(f, delimiter=',')
#    for stock, price in today_prices.items():
#        writer.writerow([stock, price])
        

def is_video(td):
    pricelabels = td('span', 'pricelabel')
    return (len(pricelabels) == 1 and \
            pricelabels[0].text.split().startwith("Video"))
#print(len([td for td in tds if not is_video(td)]))

def book_info(td):
    title = td.find("div", "thumbheader").a.text
    author_name = td.find("div", "AuthorName").text
    authors = [x.strip() for x in re.sub("^By ", "", author_name).split(",")]
    isbn_link = td.find("div", "thumbheader").a.get("href")
    isbn = re.match("/product/(.*)\.do", isbn_link).group(1)
    date = td.find("span", "directorydate").text.strip()
    
    return {
            "title": title,
            "authors": authors,
            "isbn": isbn,
            "date": date
            }

def get_year(book):
    return int(book["date"].split()[1])

if __name__ == "__main__":
    import matplotlib.font_manager as fmnt
    fname = '/usr/share/fonts/adobe-source-han-sans-cn/SourceHanSansCN-Regular.otf'
    myfont = fmnt.FontProperties(fname=fname)
    base_url = "http://shop.oreilly.com/category/browse-subjects/data.do?sortby=publicationDate&page="
    books = []
    NUM_PAGES = 31
    
    for page_num in range(1, NUM_PAGES + 1):
        print("souping page", page_num, ",", len(books), " found so far")
        url = base_url + str(page_num)
        soup = BeautifulSoup(requests.get(url).text, 'html5lib')
        
        for td in soup('td', 'thumbtext'):
            if not is_video(td):
                books.append(book_info(td))
        sleep(3)
    
    year_counts = Counter(get_year(book) for book in books if get_year(book) <= 2014)
    years = sorted(year_counts)
    book_counts = [year_counts[year] for year in years]
    plt.plot(years, book_counts)
    plt.ylabel("数据图书的数量", fontproperties=myfont)
    plt.title("数据大发展", fontproperties=myfont)
    plt.show()