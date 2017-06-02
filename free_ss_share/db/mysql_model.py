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


def insert(time, num):
    Logs(time=time, num=num).save()
    print '|    LOG: ', time, 'INSERT ', num


def get():
    for i in Logs.select():
        print i.time, i.num


# if __name__ == "__main__":
    # 创建表
    # Logs.create_table()
    # get()