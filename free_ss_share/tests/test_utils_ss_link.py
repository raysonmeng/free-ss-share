import pytest

from free_ss_share.utils import ss_link, ss_speed_test

ss_account = {
    'ip': '118.193.241.39',
    'port': '50159',
    'method': 'chacha20',
    'password': 'testpass'
}

ssr_account = {
    'ip': '118.193.241.39',
    'port': '50159',
    'method': 'chacha20',
    'password': 'testpass',
    'protocol': 'auth_sha1_v4',
    'obfs': 'tls1.2_ticket_auth'
}

link = 'ssr://MTE4LjE5My4yNDEuMzk6NTAxNTk6YXV0aF9zaGExX3Y0OmNoYWNoYTIwOnRsczEuMl90aWNrZXRfYXV0aDpkR1Z6ZEhCaGMzTT0vP3JlbWFya3M9Nkk2MzVZK1c1cHUwNWFTYTVZV042TFM1NkxTbTVZKzNMT1crcnVTL29lYVFuQ2pvaUxucGxiOUNjbVZoYXlrPQ=='

class TestClass:

    @pytest.mark.run(order=1)
    def test_encode_ss_link(self):
        link = ss_link.encode_ss_link(ip=ss_account['ip'], port=ss_account['port'], method=ss_account['method'], password=ss_account['password'])
        assert link == 'ss://Y2hhY2hhMjA6dGVzdHBhc3NAMTE4LjE5My4yNDEuMzk6NTAxNTk='

    @pytest.mark.run(order=2)
    def test_encode_ssr_link(self):
        link = ss_link.encode_ssr_link(ip=ssr_account['ip'], port=ssr_account['port'], method=ssr_account['method'], password=ssr_account['password'], protocol=ssr_account['protocol'], obfs=ssr_account['obfs'])
        assert link == 'ssr://MTE4LjE5My4yNDEuMzk6NTAxNTk6YXV0aF9zaGExX3Y0OmNoYWNoYTIwOnRsczEuMl90aWNrZXRfYXV0aDpkR1Z6ZEhCaGMzTT0='

    @pytest.mark.run(order=3)
    def test_decode_ss_link(self):
        account = ss_link.decode_link('ss://Y2hhY2hhMjA6dGVzdHBhc3NAMTE4LjE5My4yNDEuMzk6NTAxNTk=')
        assert account == ss_account

    @pytest.mark.run(order=4)
    def test_decode_ssr_link(self):
        account = ss_link.decode_link('ssr://MTE4LjE5My4yNDEuMzk6NTAxNTk6YXV0aF9zaGExX3Y0OmNoYWNoYTIwOnRsczEuMl90aWNrZXRfYXV0aDpkR1Z6ZEhCaGMzTT0=')
        assert account == ssr_account

    @pytest.mark.run(order=5)
    def test_clean_link(self):
        link = ss_link.clean_link('ssr://MTE4LjE5My4yNDEuMzk6NTAxNTk6YXV0aF9zaGExX3Y0OmNoYWNoYTIwOnRsczEuMl90aWNrZXRfYXV0aDpkR1Z6ZEhCaGMzTT0=')
        assert link == 'ssr://MTE4LjE5My4yNDEuMzk6NTAxNTk6YXV0aF9zaGExX3Y0OmNoYWNoYTIwOnRsczEuMl90aWNrZXRfYXV0aDpkR1Z6ZEhCaGMzTT0vP3JlbWFya3M9Nkk2MzVZK1c1cHUwNWFTYTVZV042TFM1NkxTbTVZKzNMT1crcnVTL29lYVFuQ2pvaUxucGxiOUNjbVZoYXlrPQ=='


