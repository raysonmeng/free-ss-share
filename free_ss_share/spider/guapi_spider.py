# -*- coding: utf-8 -*-
# https://guapi.ml/home/ 30+
import requests
from lxml import etree
# import requests.packages.urllib3.util.ssl_
# requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'
# r = requests.get('https://guapi.ml/home/')
import requests.packages.urllib3.util.ssl_
print(requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS)
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'
print(requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS)
print requests.get('https://guapi.ml/home/')


# def guapi_get_account():
#     r = requests.get('https://guapi.ml/home/')
#     selector = etree.HTML(r.content)
#     list = selector.xpath('/html/body/center/table/tbody/tr[2]/td[1]/text()')
#     for i in list:
#         print i
#
#
# if __name__ == '__main__':
#     guapi_get_account()