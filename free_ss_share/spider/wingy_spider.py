# -*- coding: utf-8 -*-
import datetime

import requests
from lxml import etree
from utils.sslink import encode_ss_link

from free_ss_share.settings.development import WINGY_URL


class WingySpider(object):

    def __init__(self):
        self._data = []
        self.result = False

    def _get_wingy_account(self):
        # 抓取原始信息
        origin_wingy_account = []
        try:
            r = requests.get(WINGY_URL)
            selector = etree.HTML(r.content)
            content = selector.xpath('/html/body/dt/text()')
            if not content:
                raise Exception
            for text in content:
                origin_wingy_account.append(text.encode('utf-8'))
            print 'wingy-spider get one account'
            self.result = True
            return origin_wingy_account
        except Exception as e:
            print "Wingy's account catch failed"
            self.result = False
            return origin_wingy_account

    def _make_json(self, data):
        # 将原始信息加工成字典
        fixed_data_list = []
        fixed_data = {
            'id': None,
            'info': {},
            'img': None,
            'account': {}
        }
        if self.result:
            # TODO:should judge the type
            # TODO:should judge the data[account] change or not, if change, update, if not change, pass.
            fixed_data['id'] = data[0].split('：')[1] + data[1].split('：')[1]
            fixed_data['result'] = self.result

            fixed_data['info']['location'] = u'火星'
            fixed_data['info']['type'] = u'Shadowsocks'
            fixed_data['info']['update_time'] = str(datetime.datetime.now()).split('.')[0]

            fixed_data['account']['ip'] = data[0].split('：')[1].decode()
            fixed_data['account']['port'] = data[1].split('：')[1].decode()
            fixed_data['account']['encryption_method'] = data[3].split(':')[1].decode()
            fixed_data['account']['password'] = data[2].split('：')[1].decode()

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
        return self._make_json(self._get_wingy_account())


if __name__ == '__main__':
    spider = WingySpider()
    print spider.feedback()
