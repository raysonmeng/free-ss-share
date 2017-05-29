# -*- coding: utf-8 -*-
import base64


def encode_ss_link(ip, port, method, password):
    ss_info = str(method) + ':' + str(password) + '@' + str(ip) + ':' + str(port)
    ss_link = 'ss://' + base64.b64encode(ss_info)
    return ss_link


def encode_ssr_link(ip, port, method, password, protocal, obfs):
    ssr_info = str(ip) + ':' + str(port) + ':' + str(protocal) + ':' + str(method) + ':' + str(obfs) + ':' + base64.b64encode(str(password))
    ssr_link = 'ssr://' + base64.b64encode(ssr_info)
    return ssr_link


def decode_base64(data):
    """Decode base64, padding being optional.

    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.

    """
    missing_padding = len(data) % 4
    if missing_padding != 0:
        data += '='* (4 - missing_padding)
    return base64.b64decode(data)


def _clean_ssr_link(link):
    info = decode_base64(link.split('://')[1]).decode()

    if '/?' in info:
        info = info.split('/?remarks')[0]

    remarks = '/?remarks='+base64.urlsafe_b64encode('获取更多免费账号,微信搜(船长Break)')
    link = 'ssr://' + base64.urlsafe_b64encode(info + remarks)
    return link


def clean_link(link):
    print 'clean link', link
    if 'ss:' in link:
        return link
    if 'ssr:' in link:
        return _clean_ssr_link(link)
