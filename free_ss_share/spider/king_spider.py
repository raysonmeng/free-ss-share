# coding=utf-8
import random
import time

from free_ss_share.db.redis_model import save
from free_ss_share.spider.doubi_spider import DoubiSpider
from free_ss_share.utils.sslink import clean_link


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

    def chew_meal(self):
        for account in self.bowl:
            if 'ss:' in account['link']:
                account['type'] = 'Shadowsocks'
            else:
                account['type'] = 'ShadowsocksR'

            account['link'] = clean_link(account['link'])

    def eat_meal(self):
        save(self.bowl)


# run spider
def run_spider():
    king = KingSpider()
    while True:
        king.get_meal()
        if not king.bowl:
            break
        king.chew_meal()
        king.eat_meal()
        sleep_time = random.randint(1, 60)
        print('Sleep {sleep_time} second!'.format(sleep_time=sleep_time))
        time.sleep(sleep_time)

if __name__ == '__main__':
    run_spider()
