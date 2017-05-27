# -*- coding: utf-8 -*-
import datetime
import json

import requests
from lxml import etree
from utils.sslink import encode_ss_link

from free_ss_share.settings.development import RY_GET_NODE_URL, RY_GET_NODE_HEADERS, RY_GET_COOKIES_URL, \
    RY_GET_COOKIES_HEADERS, RY_GET_COOKIES_PAYLOAD


class RySpider(object):

    def __init__(self):
        self.result = False

    # 更新cookies
    def update_cookies(self):
        r = requests.request("POST", RY_GET_COOKIES_URL, data=RY_GET_COOKIES_PAYLOAD, headers=RY_GET_COOKIES_HEADERS)
        RY_GET_NODE_HEADERS['cookie'] = 'sid=' + r.cookies['sid']

    def get_ry_account(self):
        # 抓取原始信息
        origin_ry_account = []
        account_location = []
        try:
            self.update_cookies()
            r = requests.get(RY_GET_NODE_URL, headers=RY_GET_NODE_HEADERS)

            selector = etree.HTML(r.content)

            # 获取账号详细页面的url列表
            part_url_list = selector.xpath('/html/body/div[1]/div/section[2]/div/div/div/div[1]/ul/li/div[2]/a/@href')

            # 获取账号的地址列表
            account_location = selector.xpath(
                '/html/body/div[1]/div/section[2]/div/div/div/div[1]/ul/li/div[2]/a/text()')

            if not part_url_list:
                raise Exception

            for part_url in part_url_list:
                r = requests.get(RY_GET_NODE_URL + part_url[6:], headers=RY_GET_NODE_HEADERS)
                selector = etree.HTML(r.content)

                # 获取账号信息
                account_info = selector.xpath(
                    '/html/body/div[1]/div/section[2]/div[1]/div[2]/div[1]/div[2]/textarea/text()')

                if not account_info:
                    continue
                origin_ry_account.append(json.loads(account_info[0]))
                print 'ry-spider get one account'

            self.result = True
            return origin_ry_account, account_location
        except Exception as e:
            print e  # "RY's account catch failed"
            self.result = False
            return origin_ry_account, account_location

    def _make_json(self, data_list, location_list):
        # 将原始信息加工成字典
        fixed_data_list = []
        for index, data in enumerate(data_list):
            fixed_data = {
                'id': None,
                'info': {},
                'img': None,
                'account': {}
            }
            if self.result:
                # TODO:should judge the type
                # TODO:should judge the data[account] change or not, if change, update, if not change, pass.
                fixed_data['id'] = str(data['server']).decode() + str(data['server_port']).decode()
                fixed_data['result'] = self.result

                fixed_data['info']['location'] = location_list[index]
                fixed_data['info']['type'] = u'Shadowsocks'
                fixed_data['info']['update_time'] = str(datetime.datetime.now()).split('.')[0]

                fixed_data['account']['ip'] = str(data['server']).decode()
                fixed_data['account']['port'] = str(data['server_port']).decode()
                fixed_data['account']['encryption_method'] = str(data['method']).decode()
                fixed_data['account']['password'] = str(data['password']).decode()

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
        account_list, location_list = self.get_ry_account()
        return self._make_json(account_list, location_list)



if __name__ == '__main__':
    spider = RySpider()
    for i in spider.feedback():
        print json.dumps(i)
    # for a in spider.feedback():
    #     print a
