# -*- coding: utf-8 -*-
import os

DOUBI_URL = 'https://doub.bid/wp-login.php?action=postpass'
DOUBI_PROTOCAL = {
    '1': 'origin',
    '2': 'verify_deflate',
    '3': 'auth_sha1_v4',
    '4': 'auth_aes128_md5',
    '5': 'auth_aes128_sha1'
}
DOUBI_OBFS = {
    '1': 'plain',
    '2': 'http_simple',
    '3': 'http_post',
    '4': 'random_head',
    '5': 'tls1.2_ticket_auth'
}
DOUBI_HEADERS = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'cache-control': "no-cache"
}
DOUBI_QUERY_STRING = {"action":"postpass"}
DOUBI_PAYLOAD = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"post_password\"\r\n\r\ndoub.io\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"Submit\"\r\n\r\n提交\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"


ARUKAS_URL = 'https://superfreess.arukascloud.io/'

URL_LIST = [
    "https://www.google.com/",
    "https://www.youtube.com/",
    "https://www.facebook.com/",
    "https://twitter.com/",
    "https://www.instagram.com/",
    "https://www.wikipedia.org/"

]

PROXIES = {'http': 'socks5://127.0.0.1:1080',
           'https': 'socks5://127.0.0.1:1080'}

# https://www.google.com/
GOOGLE_URL = "https://www.google.com/"

HEADERS = {
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
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
