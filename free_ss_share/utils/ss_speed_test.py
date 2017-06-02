# coding=utf-8
import os
import time
import json
import socket
import socks
import requests
from free_ss_share.settings.development import HEADERS, GOOGLE_URL
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


def _score(ip):

    # proxies = {
    #     "http": "socks5://127.0.0.1:1080",
    #     "https": "socks5://127.0.0.1:1080",
    # }
    # session = requests.session()
    # session.proxies = proxies

    socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 1080)
    socket.socket = socks.socksocket

    try:
        r = requests.get("http://httpbin.org/ip", timeout=30, headers=HEADERS)
    except Exception as e:
        print "|    连接代理［", ip, "］失败！", e
        return 0

    # if ip in r.content:
    #     print '|    连接代理［', ip, '］成功！'
    #     return float(str(requests.get(GOOGLE_URL, headers=HEADERS).elapsed).split(':')[-1])
    # else:
    #     print '|    连接代理［', ip, '］错误！'
    #     return 0

    if ip in r.content:
        print '|    连接代理［', ip, '］成功！'

        time.sleep(5)
        try:
            r = requests.get(GOOGLE_URL, timeout=10, headers=HEADERS)
            time1 = float(str(r.elapsed).split(':')[-1])
            print '|    访问［Google］用时：', time1, '秒'
        except Exception as e:
            time1 = 5
            print '|    访问［Google］失败！', e

        time.sleep(5)
        try:
            r = requests.get("https://www.youtube.com/", timeout=10, headers=HEADERS)
            time2 = float(str(r.elapsed).split(':')[-1])
            print '|    访问［YouTube］用时：', time2, '秒'
        except Exception as e:
            time2 = 5
            print '|    访问［YouTube］失败！', e

        time.sleep(5)
        try:
            r = requests.get("https://www.facebook.com/", timeout=10, headers=HEADERS)
            time3 = float(str(r.elapsed).split(':')[-1])
            print '|    访问［Facebook］用时：', time3, '秒'
        except Exception as e:
            time3 = 5
            print '|    访问［Facebook］失败！', e

        time.sleep(5)
        try:
            r = requests.get("https://twitter.com/", timeout=10, headers=HEADERS)
            time4 = float(str(r.elapsed).split(':')[-1])
            print '|    访问［Twitter］用时：', time4, '秒'
        except Exception as e:
            time4 = 5
            print '|    访问［Twitter］失败！', e

        time.sleep(5)
        try:
            r = requests.get("https://www.instagram.com/", timeout=10, headers=HEADERS)
            time5 = float(str(r.elapsed).split(':')[-1])
            print '|    访问［Instagram］用时：', time5, '秒'
        except Exception as e:
            time5 = 5
            print '|    访问［Instagram］失败！', e

        time.sleep(5)
        try:
            r = requests.get("https://www.wikipedia.org/", timeout=10, headers=HEADERS)
            time6 = float(str(r.elapsed).split(':')[-1])
            print '|    访问［Wikipedia］用时：', time6, '秒'
        except Exception as e:
            time6 = 5
            print '|    访问［Wikipedia］失败！', e

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
        print "|    连接代理［", ip, "］错误！"
        return 0


def test(link):
    # 1. 解析link
    # 2. 将解析结果写入shadowsocks 配置文件中
    # 3. 开启shadowsocks
    # 4. 通过代理访问google, youtube, facebook, twitter, instagram, wikipedia计算平均时间进行打分（最好写成同步的多线程代码）
    #   4.1 访问时设定timeout5s(捕获timeout异常) 大于5秒减一分
    # 5. 返回值 返回分数（1，2，3，4，5） 和 访问各个网站的用时（x.xxxxx）
    ip = write_config(decode_link(link))
    print '|    写入配置文件成功！'
    print '|    开始测试［', ip, '］！'
    os.system('ss-local -c /tmp/config.json -f /tmp/ss.pid')
    print '|    打开客户端！'
    time.sleep(3)


    # os.system('curl --socks5 127.0.0.1:1080 https://www.google.com/')


    # socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 1080)
    # socket.socket = socks.socksocket
    # print requests.get(GOOGLE_URL).text

    try:
        score = _score(ip)
    except Exception as e:
        score = 0
        os.system('kill -9 `cat /tmp/ss.pid`')
        print '|    关闭客户端！'
        return score

    os.system('kill -9 `cat /tmp/ss.pid`')
    print '|    关闭客户端！'
    return score


if __name__ == '__main__':
    test('ssr://MTA0LjE2MC4xODUuODA6NDcwNzI6YXV0aF9zaGExX3Y0OmFlcy0yNTYtY2ZiOnRsczEuMl90aWNrZXRfYXV0aDpaRzl1WjNSaGFYZGhibWN1WTI5dC8/cmVtYXJrcz01cHlzNkxTbTVZLTM1cDJsNkllcU9tUnZkV0l1YVc4dmMzTjZhR1o0')
