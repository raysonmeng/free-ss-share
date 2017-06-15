# -*- coding: utf-8 -*-
import requests
from lxml import etree
from free_ss_share.settings.development import DOUBI_URL, DOUBI_HEADERS, DOUBI_PAYLOAD, DOUBI_QUERY_STRING


def doub_get_account():
    # 抓取原始信息

    info_list = []
    try:
        r = requests.post(DOUBI_URL, data=DOUBI_PAYLOAD, headers=DOUBI_HEADERS, params=DOUBI_QUERY_STRING)
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
        return info_list

    except Exception as e:
        print e
        return info_list


if __name__ == '__main__':
    for i in doub_get_account():
        print i['ip'], i['location']
