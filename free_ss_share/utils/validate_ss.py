import os
import requests

os.system('python /home/shadowsocksr/shadowsocks/local.py -c /etc/shadowsocks.json -d start')
from free_ss_share.settings.development import HEADERS, PROXIES
r = requests.get('http://httpbin.org/ip', proxies=PROXIES, timeout=20, headers=HEADERS)
print r.text
os.system('python /home/shadowsocksr/shadowsocks/local.py -d stop')
