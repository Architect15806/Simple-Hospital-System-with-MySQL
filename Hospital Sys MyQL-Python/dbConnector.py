# -*- coding = utf-8 -*-
# @Time : 2022/5/6 19:30
# @Author : Architect
# @File : dbConnector.py
# @Software : PyCharm
import pymysql


def connect_init():
    conn = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='73755375',
        db='hospital',
        charset='utf8'
    )
    conn.autocommit(1)
    return conn