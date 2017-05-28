# coding=utf-8
import time
import random
import datetime
from free_ss_share.spider.doubi_spider import DoubiSpider
from free_ss_share.utils.sslink import clean_link
from free_ss_share.utils.db_model import save

class KingSpider(object):
    def __init__(self):
        self.spider_dict = {
            'doubi_spider': DoubiSpider(),
        }
        self.bowl = []

    def get_meal(self):
        for spider in self.spider_dict.keys():
            print(spider + ' go for meal, please wait a second.')
            meal = self.spider_dict[spider].feedback()
            self.bowl.extend(meal)
            print(spider + ' get meal successful! Totally get {num}'.format(num=str(len(meal))))

    def eat_meal(self):
        for account in self.bowl:
            if 'ss:' in account['link']:
                account['type'] = 'Shadowsocks'
            else:
                account['type'] = 'ShadowsocksR'

            account['link'] = clean_link(account['link'])
        save(self.bowl)


def run_spider():
    king = KingSpider()
    king.get_meal()
    king.eat_meal()

# run_spider()
while True:
    run_spider()
    sleep_time = random.randint(1, 5)
    print('Sleep {sleep_time} second!'.format(sleep_time=sleep_time))
    time.sleep(sleep_time)