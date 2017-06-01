# coding=utf-8
import os
import time
import json
import requests
from lxml import etree
from ss_link import decode_link


def write_config(link):
    account = decode_link(link)
    if 'protocol' in account.keys():
        config = {
            'server': account['ip'],
            'server_ipv6': '::',
            'server_port': int(account['port']),
            'local_address': '127.0.0.1',
            'local_port': 1080,
            'password': account['password'],
            'timeout': 300,
            'udp_timeout': 60,
            'method': account['method'],
            'protocol': account['protocol'],
            'protocol_param': '',
            'obfs': account['obfs'],
            'obfs_param': '',
            'fast_open': False,
            'workers': 1
        }
    else:
        config = {
            'server': account['ip'],
            'server_ipv6': '::',
            'server_port': int(account['port']),
            'local_address': '127.0.0.1',
            'local_port': 1080,
            'password': account['password'],
            'timeout': 300,
            'udp_timeout': 60,
            'method': account['method'],
            'fast_open': False,
            'workers': 1
        }
    with open('/tmp/config.json', 'w') as f:
        f.write(json.dumps(config))
    return account['ip']


def _test(ip):
    proxies = {
        "http": "socks5://127.0.0.1:1080",
        "https": "socks5://127.0.0.1:1080",
    }
    try:
        r = requests.get("http://1212.ip138.com/ic.asp", proxies=proxies, timeout=5)

        selector = etree.HTML(r.content)
        if ip in selector.xpath('/html/body/center/text()')[0]:
            print '|    连接代理［', ip, '］成功！'

            try:
                r = requests.get("https://www.google.com/", proxies=proxies, timeout=5)
                time1 = float(str(r.elapsed).split(':')[-1])
                print '|    访问［Google］用时：', time1, '秒'
            except Exception as e:
                time1 = 5
                print '|    访问［Google］失败！'

            try:
                r = requests.get("https://www.youtube.com/", proxies=proxies, timeout=5)
                time2 = float(str(r.elapsed).split(':')[-1])
                print '|    访问［YouTube］用时：', time2, '秒'
            except Exception as e:
                time2 = 5
                print '|    访问［YouTube］失败！'

            try:
                r = requests.get("https://www.facebook.com/", proxies=proxies, timeout=5)
                time3 = float(str(r.elapsed).split(':')[-1])
                print '|    访问［Facebook］用时：', time3, '秒'
            except Exception as e:
                time3 = 5
                print '|    访问［Facebook］失败！'

            try:
                r = requests.get("https://twitter.com/", proxies=proxies, timeout=5)
                time4 = float(str(r.elapsed).split(':')[-1])
                print '|    访问［Twitter］用时：', time4, '秒'
            except Exception as e:
                time4 = 5
                print '|    访问［Twitter］失败！'

            try:
                r = requests.get("https://www.instagram.com/", proxies=proxies, timeout=5)
                time5 = float(str(r.elapsed).split(':')[-1])
                print '|    访问［Instagram］用时：', time5, '秒'
            except Exception as e:
                time5 = 5
                print '|    访问［Instagram］失败！'

            try:
                r = requests.get("https://www.wikipedia.org/", proxies=proxies, timeout=5)
                time6 = float(str(r.elapsed).split(':')[-1])
                print '|    访问［Wikipedia］用时：', time6, '秒'
            except Exception as e:
                time6 = 5
                print '|    访问［Wikipedia］失败！'

            round_time = round((time1 + time2 + time3 + time4 + time5 + time6) / 6, 2)
            print '|    平均用时约：', round_time, '秒'
            if round_time < 1.00:
                score = 5
                print '|    得分★★★★★'
            elif 1.00 <= round_time < 2.00:
                score = 4
                print '|    得分★★★★☆'
            elif 2.00 <= round_time < 3.00:
                score = 3
                print '|    得分★★★☆☆'
            elif 3.00 <= round_time < 4.00:
                score = 2
                print '|    得分★★☆☆☆'
            elif 4.00 <= round_time < 5.00:
                score = 1
                print '|    得分★☆☆☆☆'
            elif 5.00 <= round_time:
                score = 0
                print '|    得分☆☆☆☆☆'
            return score
        else:
            print "|    Proxies can't use!"
            return 0
    except Exception as e:
        print "|    Proxies can't use!"
        return 0

def test(link):
    # 1. 解析link
    # 2. 将解析结果写入shadowsocks 配置文件中
    # 3. 开启shadowsocks
    # 4. 通过代理访问google, youtube, facebook, twitter, instagram, wikipedia计算平均时间进行打分（最好写成同步的多线程代码）
    #   4.1 访问时设定timeout5s(捕获timeout异常) 大于5秒减一分
    # 5. 返回值 返回分数（1，2，3，4，5） 和 访问各个网站的用时（x.xxxxx）
    ip = write_config(link)
    print '|    开始测试［', ip, '］！'
    os.system('sslocal -c /tmp/config.json -d start')
    try:
        score = _test(ip)
    except Exception as e:
        score = 0
        return score
    finally:
        os.system('sslocal -d stop')
        time.sleep(1)

    os.system('sslocal -d stop')
    time.sleep(1)
    return score


if __name__ == '__main__':
    test('ssr://MTA0LjE2MC4xODUuODA6NDcwNzI6YXV0aF9zaGExX3Y0OmFlcy0yNTYtY2ZiOnRsczEuMl90aWNrZXRfYXV0aDpaRzl1WjNSaGFYZGhibWN1WTI5dC8/cmVtYXJrcz01cHlzNkxTbTVZLTM1cDJsNkllcU9tUnZkV0l1YVc4dmMzTjZhR1o0')
