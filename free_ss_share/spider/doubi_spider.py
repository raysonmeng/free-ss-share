# -*- coding: utf-8 -*-
import requests
from lxml import etree

from free_ss_share.settings.development import DOUBI_URL


class DoubiSpider(object):

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

        except Exception as e:
            print e

            return info_list

    def feedback(self):
        return self._get_info_list()


if __name__ == '__main__':
    spider = DoubiSpider()
    print len(spider.feedback())
    for i in spider.feedback():
        print i['ip'], i['location']
