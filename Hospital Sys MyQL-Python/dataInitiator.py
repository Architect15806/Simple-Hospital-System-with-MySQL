# -*- coding = utf-8 -*-
# @Time : 2022/5/6 19:19
# @Author : Architect
# @File : dataInitiator.py
# @Software : PyCharm

# 连接数据库
import sys
import traceback
import pymysql
from prettytable import PrettyTable

from dataDictionary import DataDictionary
from dataReader import DataReaderIter
from dbConnector import connect_init


def db_table_init(conn):
    cursor = conn.cursor()
    cursor.callproc("hospital_table_init")
    conn.commit()
    print("--数据库系统 %s 已结构初始化" % str(conn.db)[1:])

    try:
        cursor.execute("SHOW TABLES")
        results = (cursor.fetchall())
        print("----可用关系表：")
        i = 0
        for tab in results:
            if i % 3 == 0:
                print("------", end="")
            print("【" + str(tab)[2:-3] + "】", end=" ")
            i = i + 1
            if i % 3 == 0:
                print()
    except Exception as error:
        print(error)
    finally:
        cursor.close()


# 从data.xlsx插入数据操作
def insert_from_xlsx(conn):
    cursor = conn.cursor()
    print("--初始数据正在载入数据库 %s" % str(conn.db)[1:])
    try:
        insert_single_table(conn, cursor, 'doctors')
        insert_single_table(conn, cursor, 'nurses')
        insert_single_table(conn, cursor, 'patients')
        insert_single_table(conn, cursor, 'beds')
        insert_single_table(conn, cursor, 'drugs')
        insert_single_table(conn, cursor, 'dp_rel')
        insert_single_table(conn, cursor, 'drug_sell')
        insert_single_table(conn, cursor, 'host_rel')
    except:
        traceback.print_exc()
        # 发生错误时回滚
        conn.rollback()
    finally:
        # 关闭游标连接
        cursor.close()
    #     # 关闭数据库连接
    #     conn.close()


# 格式化插入一张表的数据
def insert_single_table(conn, cursor, table_name):
    count = 0
    dataReaderIter = DataReaderIter(table_name)
    for row_tuple in dataReaderIter:
        count += cursor.execute(DataDictionary.format_dict[table_name] % row_tuple)
        conn.commit()
    print("----成功插入 %d 条数据到 '%s' 数据表" % (count, table_name))


def db_reference_init(conn):
    cursor = conn.cursor()
    cursor.callproc("hospital_reference_init")
    conn.commit()
    cursor.close()
    print("--数据库 %s 中的参照关系已成功部署" % str(conn.db)[1:])

def db_view_init(conn):
    cursor = conn.cursor()
    cursor.callproc("hospital_view_init")
    conn.commit()
    cursor.close()
    print("--数据库 %s 中的视图结构已成功部署" % str(conn.db)[1:])


def db_init():
    conn = connect_init()
    print("开始数据库系统初始化")
    try:
        db_table_init(conn)
        insert_from_xlsx(conn)
        db_reference_init(conn)
        db_view_init(conn)
    except:
        traceback.print_exc()
    finally:
        # 关闭数据库连接
        conn.close()
