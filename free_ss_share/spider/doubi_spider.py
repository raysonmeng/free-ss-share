# -*- coding: utf-8 -*-
import requests
from lxml import etree

from free_ss_share.settings.development import DOUBI_URL


class DoubiSpider(object):

    def __init__(self):
        self.result = False

    def _get_info_list(self):
        # 抓取原始信息

        info_list = []
        try:
            r = requests.get(DOUBI_URL)
            selector = etree.HTML(r.content)
            url_list = selector.xpath('/html/body/section/div[2]/div/div[1]/div[6]/div/table/tbody/tr/td[7]/a[@class="dl1"]/@href')
            location_list1 = selector.xpath('/html/body/section/div[2]/div/div[1]/div[6]/div/table/tbody/tr/td[1]/strong/span/text()')
            location_list2 = selector.xpath('/html/body/section/div[2]/div/div[1]/div[6]/div/table/tbody/tr/td[1]/text()')
            location_list = location_list1 + location_list2

            for i in range(len(url_list)):
                ip = selector.xpath('/html/body/section/div[2]/div/div[1]/div[6]/div/table/tbody/tr['+ str(i+2) + ']/td[2]/text()')
                if ip:
                    info_list.append(
                        {
                            'ip': ip[0],
                            'location': location_list[i],
                            'link': url_list[i].split('text=')[1]
                        }
                    )
                    # print info_list[-1]
            return info_list

        # 爬虫只获取ip和链接
        # 将ip和链接返回给king
        # flask－admin 调度 king
        # king 调度爬虫 获取爬虫拿到的ip和链接
        # 由king将ip转为location，再加上时间然后入库
        # 入库操作：
        # 1:获取redis中的数据(old_data)
        # 2:将old_data与要入库的数据(new_data)取交集(list)
        # 3:redis.delete(old_data - list)
        # 4:redis.add(new_data - list)
        # 5:将redis完整的数据导入到mysql作为持久存储等待下一次爬取结果
        # flask获取 直接调取数据库get
        # info = {
        #     'ip': '',
        #     'location': '',
        #
        # }

        except Exception as e:
            print (e)  # "Wingy's account catch failed"
            self.result = False
            return info_list

    def feedback(self):
        return self._get_info_list()



if __name__ == '__main__':
    spider = DoubiSpider()
    for i in spider.feedback():
        print(i)
