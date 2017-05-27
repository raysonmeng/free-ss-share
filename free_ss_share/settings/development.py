import os

DOUBI_URL = 'https://doub.bid/sszhfx/'
DOUBI_PROTOCAL= {
    '1': 'origin',
    '2': 'verify_deflate',
    '3': 'auth_sha1_v4',
    '4': 'auth_aes128_md5',
    '5': 'auth_aes128_sha1'
}
DOUBI_OBFS= {
    '1': 'plain',
    '2': 'http_simple',
    '3': 'http_post',
    '4': 'random_head',
    '5': 'tls1.2_ticket_auth'
}

FREE_URL = 'http://freess.org/'
S8_URL = 'http://ss.shadowsocks8.cc/'
WINGY_URL = 'https://www.wingy.site/freess/'
ARUKAS_URL = 'https://superfreess.arukascloud.io/'

RY_GET_COOKIES_URL = 'https://ry-ss.me/auth/login'
RY_GET_COOKIES_PAYLOAD = "email=rayson951005%40gmail.com&passwd=mxl951005&remember_me=week"
RY_GET_COOKIES_HEADERS = {
    'host': "ry-ss.me",
    'connection': "keep-alive",
    'content-length': "64",
    'accept': "application/json, text/javascript, */*; q=0.01",
    'origin': "https://ry-ss.me",
    'x-requested-with': "XMLHttpRequest",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
    'content-type': "application/x-www-form-urlencoded",
    'dnt': "1",
    'referer': "https://ry-ss.me/auth/login",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "zh-CN,zh;q=0.8,en;q=0.6",
    'cache-control': "no-cache",
    }

RY_GET_NODE_URL = 'https://ry-ss.me/user/node'
RY_GET_NODE_HEADERS = {
    'host': "ry-ss.me",
    'connection': "keep-alive",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    'dnt': "1",
    'referer': "https://ry-ss.me/user",
    'accept-encoding': "gzip, deflate, sdch, br",
    'accept-language': "zh-CN,zh;q=0.8,en;q=0.6",
    }


DB_HOST = os.environ.get('DB_HOST') or 'localhost'
DB_PORT = os.environ.get('DB_PORT') or 28015
DB_NAME = 'ss_db'
TABLE_NAME = 'account'


'''
{
    "provider": "Wingy",
    "location": ""
    "type": "ss",
    "update_time": "2017-04-07 18:49:31",
    "id": "ip:port"
    "img": "img path"
    "account": {
        "ip": "freess.wingy.site",
        "port": "9999",
        "encryption_method": "9449",
        "password": "aes-256-cfb",
        "protocal": "auth_aes128_md5",
        "obfs": "http_simple"
    }
}
'''