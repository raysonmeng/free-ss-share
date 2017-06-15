import pytest
from free_ss_share.spider.doubi_spider import doub_get_account
from free_ss_share.spider.guagua_spider import guagua_get_account


def test_doub_spider():
    print '\nStart test doubi spider!'
    account = doub_get_account()
    assert type(account) == list
    assert account != []
    print '\nFinish test doubi spider!'

def test_guagua_spider():
    print '\nStart test guagua spider!'
    account = guagua_get_account()
    assert type(account) == list
    assert account != []
    print '\nFinish test guagua spider!'
