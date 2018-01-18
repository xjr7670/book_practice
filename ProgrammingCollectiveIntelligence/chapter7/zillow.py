#!/usr/bin/env python
#-*- coding:utf-8 -*-

import xml.dom.minidom
from urllib import request
import xmltodict
import requests


zwskey = "X1-ZWz1chwxis15aj_9skq6"

def getaddressdata(address, city):
    escad = address.replace(' ', '+')

    # 构建URL
    url = 'http://www.zillow.com/webservice/GetDeepSearchResults.htm?'
    url += 'zws-id=%s&address=%s&citystatezip=%s' % (zwskey, escad, city)

    try:
        doc = xml.dom.minidom.parseString(requests.get(url).text)
        code = doc.getElementsByTagName('code')[0].firstChild.data
    except xml.parsers.expat.ExpatError:
        return None

    if code != '0':
        return None

    try:
        zipcode = doc.getElementsByTagName('zipcode')[0].firstChild.data
        use = doc.getElementsByTagName('useCode')[0].firstChild.data
        year = doc.getElementsByTagName('yearBuilt')[0].firstChild.data
        bath = doc.getElementsByTagName('bathrooms')[0].firstChild.data
        bed = doc.getElementsByTagName('bedrooms')[0].firstChild.data
        rooms = doc.getElementsByTagName('totalRooms')[0].firstChild.data
        price = doc.getElementsByTagName('amount')[0].firstChild.data
    except:
        return None

    return (zipcode, use, int(year), float(bath), int(bed), int(rooms), price)


def getaddressdata2(address, city):
    escad = address.replace(' ', '+')

    # 构建URL
    url = 'http://www.zillow.com/webservice/GetDeepSearchResults.htm?'
    url += 'zws-id=%s&address=%s&citystatezip=%s' % (zwskey, escad, city)

    # 解析XML形式的返回结果
    xml = request.urlopen(url).read()
    dict_xml = xmltodict.parse(xml)


    # 提取有关该房产的信息
    try:
        # 把结果集取出来
        result = dict_xml['SearchResults:searchresults']['response']['results']['result'][0]
        zipcode = result['address']['zipcode']
        use = result['useCode']
        year = result['yearBuilt']
        bath = result['bathrooms']
        bed = result['bedrooms']
        rooms = result['totalRooms']
        price = result['zestimate']['amount']['#text']
    except:
        return None

    return (zipcode, use, int(year), float(bath), int(bed), int(rooms), price)


def getpricelist():
    l1 = []
    for line in open('addresslist.txt'):
        data = getaddressdata(line.strip(), 'Cambridge,MA')
        l1.append(data)
    return l1

