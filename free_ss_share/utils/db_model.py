# coding=utf-8
from redis import Redis



redis = Redis(host='redis', port=6379)


def save(account_list):
    redis.flushall()
    for account in account_list:
        print('[INSERT] ', account)
        # redis.hset('account', 'ip', account['ip'])
        redis.hset(account['ip'], 'location', account['location'])
        redis.hset(account['ip'], 'type', account['type'])
        redis.hset(account['ip'], 'link', account['link'])
        redis.hset(account['ip'], 'update_time', account['update_time'])

    print(redis.dbsize())


def get():
    account_list = []
    for i in redis.keys():
        account_list.append(redis.hgetall(i))
    return account_list

