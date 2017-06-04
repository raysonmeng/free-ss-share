import pytest

from free_ss_share.utils import ss_link, ss_speed_test


class TestSSLinkClass:

    @pytest.mark.run(order=1)
    def test_encode_ss_link(self):
        assert 1 == 1

    @pytest.mark.run(order=2)
    def test_encode_ssr_link(self):
        assert 1 == 1

    @pytest.mark.run(order=3)
    def test_decode_ss_link(self):
        assert 1 == 1

    @pytest.mark.run(order=4)
    def test_decode_ssr_link(self):
        assert 1 == 1

    @pytest.mark.run(order=5)
    def test_clean_link(self):
        assert 1 == 1


class TestSSSpeedTestClass:

    @pytest.mark.run(order=1)
    def test_encode_ss_link(self):
        assert 1 == 1

    @pytest.mark.run(order=2)
    def test_encode_ssr_link(self):
        assert 1 == 1

    @pytest.mark.run(order=3)
    def test_decode_ss_link(self):
        assert 1 == 1

    @pytest.mark.run(order=4)
    def test_decode_ssr_link(self):
        assert 1 == 1

    @pytest.mark.run(order=5)
    def test_clean_link(self):
        assert 1 == 1

class TestGuaGuaSpider:
    pass


class TestDoubiSpider:
    pass