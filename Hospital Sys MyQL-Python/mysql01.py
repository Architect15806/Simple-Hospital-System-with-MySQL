# -*- coding = utf-8 -*-
# @Time : 2022/4/23 10:20
# @Author : Architect
# @File : mysql01.py
# @Software : PyCharm


import pymysql.cursors

# 连接数据库
conn = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='73755375',
    db='learningdb03',
    charset='utf8'
)
conn.autocommit(1)
cursor = conn.cursor()

try:
    # 第一题：查询指定课程
    c_name = '"离散数学"'
    count = cursor.execute('SELECT * FROM course where cname = %s' % c_name)
    print('total records:', cursor.rowcount)

    results = cursor.fetchall()
    for row in results:
        cno = row[0]
        cname = row[1]
        cpno = row[2]
        ccredit = row[3]
        print(cno, '\t', cname, '\t\t', cpno, '\t\t', ccredit)
except:
    import traceback

    traceback.print_exc()
    # 发生错误时回滚
    conn.rollback()
finally:
    # 关闭游标连接
    cursor.close()
    # 关闭数据库连接
    conn.close()
