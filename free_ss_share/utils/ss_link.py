# -*- coding: utf-8 -*-
import base64


def encode_ss_link(ip, port, method, password):
    ss_info = str(method) + ':' + str(password) + '@' + str(ip) + ':' + str(port)
    ss_link = 'ss://' + base64.b64encode(ss_info)
    return ss_link


def encode_ssr_link(ip, port, method, password, protocol, obfs):
    ssr_info = str(ip) + ':' + str(port) + ':' + str(protocol) + ':' + str(method) + ':' + str(obfs) + ':' + base64.b64encode(str(password))
    ssr_link = 'ssr://' + base64.b64encode(ssr_info)
    return ssr_link


def _decode_base64(data):
    """Decode base64, padding being optional.

    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.

    """
    missing_padding = len(data) % 4
    if missing_padding != 0:
        data += '='* (4 - missing_padding)
    return base64.b64decode(data)


def _decode_ss_link(link):
    info = _decode_base64(link.split('://')[1])
    account = {
        'ip': info.split('@')[1].split(':')[0],
        'port': info.split('@')[1].split(':')[1],
        'method': info.split('@')[0].split(':')[0],
        'password': info.split('@')[0].split(':')[1]
    }
    return account


def _decode_ssr_link(link):
    info = _decode_base64(link.split('://')[1])
    if '/?' in info:
        info = info.split('/?')[0]
    account = {
        'ip': info.split(':')[0],
        'port': info.split(':')[1],
        'method': info.split(':')[3],
        'password': _decode_base64(info.split(':')[-1]),
        'protocol': info.split(':')[2],
        'obfs': info.split(':')[4]
    }
    return account


def decode_link(link):
    if 'ss:' in link:
        return _decode_ss_link(link)
    if 'ssr:' in link:
        return _decode_ssr_link(link)


def _clean_ssr_link(link):
    info = _decode_base64(link.split('://')[1]).decode()
    if '/?' in info:
        info = info.split('/?')[0]

    # remarks = '/?remarks='+base64.urlsafe_b64encode('获取更多免费账号,微信搜(船长Break)')
    link = 'ssr://' + base64.urlsafe_b64encode(info + '/?remarks=6I635Y+W5pu05aSa5YWN6LS56LSm5Y+3LOW+ruS/oeaQnCjoiLnplb9CcmVhayk=')
    return link


def clean_link(link):
    if 'ss:' in link:
        return link
    if 'ssr:' in link:
        return _clean_ssr_link(link)
