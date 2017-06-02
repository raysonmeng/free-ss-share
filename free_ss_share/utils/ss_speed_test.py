# coding=utf-8
import os
import json
import socket
import socks
import requests
import threading
from free_ss_share.settings.development import HEADERS, GOOGLE_URL, URL_LIST, PROXIES
from ss_link import decode_link

#


def write_config(account):

    if 'protocol' in account.keys():
        config = {
            'server': account['ip'],
            'server_port': account['port'],
            'local_address': '127.0.0.1',
            'local_port': 1080,
            'password': account['password'],
            'timeout': 300,
            'udp_timeout': 60,
            'method': account['method'],
            'protocol': account['protocol'],
            'protocol_param': '',
            'obfs': account['obfs'],
            'obfs_param': ''
        }
    else:
        config = {
            'server': account['ip'],
            'server_port': account['port'],
            'local_address': '127.0.0.1',
            'local_port': 1080,
            'password': account['password'],
            'timeout': 300,
            'udp_timeout': 60,
            'method': account['method']
        }
    with open('/tmp/config.json', 'w') as f:
        f.write(json.dumps(config))
    return account['ip']


time_dict = {}
class TestThread(threading.Thread):
    def __init__(self, url):
        super(TestThread, self).__init__()
        self.url = url


    def run(self):
        try:
            r = requests.get(self.url, proxies=PROXIES, timeout=20, headers=HEADERS)
            use_time = float(str(r.elapsed).split(':')[-1])

            time_dict[self.url] = use_time
            print '|    访问［' + self.url + '］用时：', use_time, '秒'
        except Exception as e:
            time_dict[self.url] = -1
            print '|    访问［' + self.url + '］失败！', e


def test(link):
    ip = write_config(decode_link(link))
    print '|    写入配置文件成功！'
    print '|    开始测试［', ip, '］！'
    os.system('ss-local -c /tmp/config.json -f /tmp/ss.pid')
    print '|    打开客户端！'

    thread_list = []
    for url in URL_LIST:
        test_thread = TestThread(url)
        thread_list.append(test_thread)

    print '|    开始测试代理有效性！'
    try:
        if ip in requests.get('http://httpbin.org/ip', proxies=PROXIES, timeout=20, headers=HEADERS).content:
            print '|    代理有效！'
    except Exception as e:
        print '|    代理无效！', e
        return 0

    print '|    开始进行网速测试！'
    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        if thread.isAlive():
            thread.join()
    print '|    网速测试结束。'


    os.system('kill -9 `cat /tmp/ss.pid`')
    print '|    关闭客户端！'
    time_list = time_dict.values()
    valid_time_list = []
    unvalid_time_times = 0

    ave_time = 0
    for time in time_list:
        if time != -1:
            valid_time_list.append(time)
        else:
            unvalid_time_times += 1

    print '|    有效时间', valid_time_list

    if len(valid_time_list):
        ave_time = sum(valid_time_list)/len(valid_time_list)
    print '|    平均时间', ave_time

    if ave_time == 0:
        return 0
    if ave_time < 2:
        return 5 - unvalid_time_times*0.5
    elif 2 <= ave_time < 4:
        return 4 - unvalid_time_times*0.5
    elif 4 <= ave_time < 6:
        return 3 - unvalid_time_times*0.5
    elif 6 <= ave_time < 8:
        return 2 - unvalid_time_times*0.5
    elif 8 <= ave_time < 10:
        return 1 - unvalid_time_times*0.5
    elif 10 <= ave_time:
        return 0


if __name__ == '__main__':
    test('ssr://MTA0LjE2MC4xODUuODA6NDcwNzI6YXV0aF9zaGExX3Y0OmFlcy0yNTYtY2ZiOnRsczEuMl90aWNrZXRfYXV0aDpaRzl1WjNSaGFYZGhibWN1WTI5dC8/cmVtYXJrcz01cHlzNkxTbTVZLTM1cDJsNkllcU9tUnZkV0l1YVc4dmMzTjZhR1o0')
