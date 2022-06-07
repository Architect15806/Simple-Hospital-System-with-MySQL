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
    # 第二题：更新指定分数
    new_grade = '100'
    c_no = '1'
    s_no = '201215121'
    count = cursor.execute(
        'UPDATE sc SET grade = %s WHERE sno = %s AND cno = %s' % (new_grade, s_no, c_no))
    conn.commit()
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
