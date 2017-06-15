# coding=utf-8
from peewee import *

db = MySQLDatabase("mysitedb", host="db", port=3306, user="root", passwd="951005")
db.connect()


class BaseModel(Model):

    class Meta:
        database = db


class Logs(BaseModel):
    time = DateTimeField()
    num = IntegerField()
    # exception = TextField(default='No Error')


def insert(time, num):
    creat_table()
    Logs(time=time, num=num).save()
    print '|    LOG: ', time, 'INSERT ', num


def get():
    for i in Logs.select():
        print i.time, i.num


def creat_table():
    if 'logs' in db.get_tables():
        print '|    表［logs］存在，无需创建'
    else:
        Logs.create_table()
        print '|    表［logs］创建成功！'

# if __name__ == "__main__":
    # 创建表
    # Logs.create_table()
    # get()