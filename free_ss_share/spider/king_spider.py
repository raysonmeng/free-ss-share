# coding=utf-8
import time
import random
import threading
from free_ss_share.db.redis_model import save
from free_ss_share.spider.doubi_spider import doub_get_account
from free_ss_share.spider.guagua_spider import guagua_get_account
from free_ss_share.utils.ss_link import clean_link
from free_ss_share.utils.ss_speed_test import test


bowl = []

class SpiderThread(threading.Thread):
    def __init__(self, spider):
        super(SpiderThread, self).__init__()
        self.name = spider['name']
        self.func = spider['func']


    def run(self):
        print('|    ' + self.name + ' 爬虫启动成功！开始捕食，请稍等......')
        meal = self.func()
        bowl.extend(meal)
        print('|    ' + self.name + ' 捕食成功，共获取到 {num} 条账号信息！'.format(num=str(len(meal))))

class KingSpider(object):
    def __init__(self):
        self.spider_list = [

            {
                'name': 'Doubi',
                'func': doub_get_account
            },

            {
                'name': 'Guagua',
                'func': guagua_get_account
            }
        ]

    def get_meal(self):
        print '+-----------------------STRAT GET MEAL!----------------------------+'
        thread_list = []
        for spider in self.spider_list:
            spider_thread = SpiderThread(spider)
            thread_list.append(spider_thread)

        print '|    开始启动子爬虫线程'
        for thread in thread_list:
            thread.start()

        for thread in thread_list:
            if thread.isAlive():
                thread.join()
        print '+-----------------------FINISH GET MEAL!----------------------------+'
        print '+                                                                   +'

    def chew_meal(self):
        print '+                                                                   +'
        print '+-----------------------STRAT CHEW MEAL!----------------------------+'
        for account in bowl:
            if 'ss:' in account['link']:
                account['type'] = 'Shadowsocks'
            else:
                account['type'] = 'ShadowsocksR'
            print '|'
            print '|----开始评分系统，请稍等。。。-------------------------------------+'
            account['score'] = test(account['link'])  # 加这一步每个代理需要多耗时10s
            print '|----评分系统结束，最终得分{score}。------------------------------------+'.format(score=str(account['score']))
            account['link'] = clean_link(account['link'])
            time.sleep(2)
        print '+-----------------------FINISH CHEW MEAL!---------------------------+'
        print '+                                                                   +'

    def eat_meal(self):
        save(bowl)


# run spider
def run_spider():
    global bowl
    king = KingSpider()
    while True:
        start_time = time.time()
        king.get_meal()
        if not bowl:
            break
        king.chew_meal()
        king.eat_meal()
        bowl = []
        sleep_time = random.randint(1, 60)
        print('\n|    Sleep {sleep_time} second!  _(:3」∠)_ 本次用时{use_time}\n'.format(sleep_time=sleep_time,use_time=time.time()-start_time))
        time.sleep(sleep_time)

if __name__ == '__main__':
    run_spider()
