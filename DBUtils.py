#!/usr/bin/python3
# encoding='utf-8'
# author:weibk
# @time:2021/10/6 19:18

import pymysql


class DatabaseConnect:
    def __init__(self, host="localhost", post=3306, user="root",
                 password="root",
                 database="", charset="utf8", cursorclass="Cursor"):
        self.connect = pymysql.connect(host=host, port=post, user=user,
                                       password=password, database=database,
                                       charset=charset)
        self.cursor = self.connect.cursor(cursor=cursorclass)

    def __enter__(self):
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connect.commit()
        self.cursor.close()
        self.connect.close()


def update(sql, params, database="db"):
    with DatabaseConnect(password="123456", database=database,
                         cursorclass=pymysql.cursors.DictCursor) as cursor:
        cursor.execute(sql, params)


def query(sql, parmas=[], size=0, database="db"):
    with DatabaseConnect(password="123456", database=database,
                         cursorclass=pymysql.cursors.DictCursor) as cursor:
        cursor.execute(sql, parmas)
        if size == 0:
            return cursor.fetchall()
        elif size == 1:
            return cursor.fetchone()
        else:
            return cursor.fetchmany(size)
