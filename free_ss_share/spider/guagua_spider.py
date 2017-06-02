# -*- coding: utf-8 -*-
# http://guaguass.lol/   20
import json
import requests
from free_ss_share.utils.ss_link import encode_ss_link


def guagua_get_account():
    r = requests.get('http://guaguass.lol/api.php?email=&password=')
    html = r.content
    account_list = []
    for i in json.loads(html)['data']:
        password = i['attributes']['cmd'].split(' ')[3]
        method = i['attributes']['cmd'].split(' ')[5]
        for j in i['attributes']['port_mappings']:
            ip = '.'.join(j[0]['host'].split('.')[0].split('-')[1:])
            port = j[0]['service_port']
            account_list.append(
                {
                    'ip': ip,
                    'location': '日本 - 樱花Docker',
                    'link': encode_ss_link(ip, port, method, password)
                }
            )
    return account_list

if __name__ == '__main__':
    guagua_get_account()