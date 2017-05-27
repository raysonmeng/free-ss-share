# coding=utf-8
import requests
from lxml import etree

def get_location(ip):
    r = requests.get('http://ip138.com/ips1388.asp?ip='+ip+'&action=2')
    selector = etree.HTML(r.content)
    try:
        location = selector.xpath('//ul[@class="ul1"]/li[1]/text()')[0].split(u'\uff1a')[1]
        if ' ' in location:
            location = location.split(' ')[0]
            # print type(location), location
    except Exception as e:
        return '未知'
    return location

