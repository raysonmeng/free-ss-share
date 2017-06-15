# coding=utf-8
import time
from redis import Redis
from mysql_model import insert

redis = Redis(host='redis', port=6379)


def save(account_list):
    print '+                                                                   +'
    print '+------------------------START EAT MEAL!----------------------------+'
    redis.flushall()
    i = 0
    for account in account_list:
        print account
        if account['score'] <= 0:
            continue
        redis.hset(account['ip'], 'location', account['location'])
        redis.hset(account['ip'], 'type', account['type'])
        redis.hset(account['ip'], 'link', account['link'])
        redis.hset(account['ip'], 'score', account['score'])
        print '|    Eat ', account['ip'], account['location'], account['type']
        i += 1
    # insert(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), str(i))
    print '+----------------------FINISH EAT MEAL!-----------------------------+'
    print '+                                                                   +'


def flushall():
    redis.flushall()


def get():
    account_list = []
    for i in redis.keys():
        account_list.append(redis.hgetall(i))
    return account_list
