# -*- coding: utf-8 -*-
import datetime
import json

import requests
from lxml import etree
from utils.sslink import encode_ss_link

from free_ss_share.settings.development import ARUKAS_URL


class ArukasSpider(object):

    def __init__(self):
        self.result = False

    def _get_arukas_account(self):
        # 抓取原始信息
        origin_arukas_account = []
        try:
            r = requests.get(ARUKAS_URL)
            selector = etree.HTML(r.content)
            # main > div.content > small > div > fieldset:nth-child(1) > legend > b > a
            content = selector.xpath('/html/body/div[@id="main"]/div[@class="content"]//div/fieldset//b/a/@href')
            if not content:
                raise Exception
            content = list(set(content))
            for uuid in content:
                r = requests.get(ARUKAS_URL+uuid)
                for text in r.content[1:-1].replace('},{', '}，{').split('，'):
                    origin_arukas_account.append(json.loads(text))
                    print 'arukas-spider get one account'
            self.result = True
            return origin_arukas_account
        except Exception as e:
            print "Arukas's account catch failed"
            self.result = False
            return origin_arukas_account

    def _make_json(self, data_list):
        # 将原始信息加工成字典
        fixed_data_list = []
        for data in data_list:
            fixed_data = {
                'id': None,
                'info': {},
                'img': None,
                'account': {}
            }
            if self.result:
                # TODO:should judge the type
                # TODO:should judge the data[account] change or not, if change, update, if not change, pass.
                fixed_data['id'] = str(data['server']) + str(data['server_port'])
                fixed_data['result'] = self.result

                fixed_data['info']['location'] = u'火星'
                fixed_data['info']['type'] = u'Shadowsocks'
                fixed_data['info']['update_time'] = str(datetime.datetime.now()).split('.')[0]

                fixed_data['account']['ip'] = data['server']
                fixed_data['account']['port'] = data['server_port']
                fixed_data['account']['encryption_method'] = data['method']
                fixed_data['account']['password'] = data['password']

                fixed_data['img'] = encode_ss_link(fixed_data['account']['ip'],
                                                   fixed_data['account']['port'],
                                                   fixed_data['account']['encryption_method'],
                                                   fixed_data['account']['password']
                                                   ).decode()
            else:
                fixed_data['result'] = self.result
            fixed_data_list.append(fixed_data)
        return fixed_data_list

    def feedback(self):
        return self._make_json(self._get_arukas_account())


if __name__ == '__main__':
    spider = ArukasSpider()
    print spider.feedback()
