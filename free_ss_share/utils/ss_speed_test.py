# coding=utf-8
import requests
from lxml import etree

proxies = {
    "http": "socks5://127.0.0.1:1086",
    "https": "socks5://127.0.0.1:1086",
}

r = requests.get("http://1212.ip138.com/ic.asp", proxies=proxies)
selector = etree.HTML(r.content)
if '118.193.241.39' in selector.xpath('/html/body/center/text()')[0]:
    print '连接代理［118.193.241.39］成功！'
    r = requests.get("https://www.google.com/", proxies=proxies)
    time1 = float(str(r.elapsed).split(':')[-1])
    print '访问［Google］用时：', time1, '秒'

    r = requests.get("https://www.youtube.com/", proxies=proxies)
    time2 = float(str(r.elapsed).split(':')[-1])
    print '访问［YouTube］用时：', time2, '秒'

    r = requests.get("https://www.facebook.com/", proxies=proxies)
    time3 = float(str(r.elapsed).split(':')[-1])
    print '访问［Facebook］用时：', time3, '秒'

    r = requests.get("https://twitter.com/", proxies=proxies)
    time4 = float(str(r.elapsed).split(':')[-1])
    print '访问［Twitter］用时：', time4, '秒'

    r = requests.get("https://www.instagram.com/", proxies=proxies)
    time5 = float(str(r.elapsed).split(':')[-1])
    print '访问［Instagram］用时：', time5, '秒'

    r = requests.get("https://www.wikipedia.org/", proxies=proxies)
    time6 = float(str(r.elapsed).split(':')[-1])
    print '访问［Wikipedia］用时：', time6, '秒'

    round_time = round((time1+time2+time3+time4+time5+time6)/6, 2)
    print '平均用时约：', round_time, '秒'
    if round_time <= 1.00:
        print '得分★★★★★'
    elif 1.00 < round_time <= 2.00:
        print '得分★★★★☆'
    elif 2.00 < round_time <= 3.00:
        print '得分★★★☆☆'
    elif 3.00 < round_time <= 4.00:
        print '得分★★☆☆☆'
    elif 4.00 < round_time <= 5.00:
        print '得分★☆☆☆☆'
    elif 5.00 < round_time:
        print '得分☆☆☆☆☆'
else:
    print "Proxies can't use!"


def test(link):
    # 1. 解析link
    # 2. 将解析结果写入shadowsocks 配置文件中
    # 3. 开启shadowsocks
    # 4. 通过代理访问google, youtube, facebook, twitter, instagram, wikipedia计算平均时间进行打分（最好写成同步的多线程代码）
    #   4.1 访问时设定timeout5s(捕获timeout异常) 大于5秒减一分
    # 5. 返回值 返回分数（1，2，3，4，5） 和 访问各个网站的用时（x.xxxxx）
    return 5