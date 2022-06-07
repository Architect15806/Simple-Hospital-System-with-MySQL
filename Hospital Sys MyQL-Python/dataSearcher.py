# -*- coding = utf-8 -*-
# @Time : 2022/5/7 19:41
# @Author : Architect
# @File : dataSearcher.py
# @Software : PyCharm
import sys

from prettytable import PrettyTable

from dataDictionary import DataDictionary
from dbConnector import connect_init


def showPayCheck(pno):
    # SELECT * FROM drugs_pay_view WHERE patient_no = 'P0001'
    conn = connect_init()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT drug_name, drug_price, drug_number, total_price FROM drugs_pay_view WHERE patient_no = '%s'" % pno)
        results = cursor.fetchall()
        if results:
            table = PrettyTable(["药品名称", "药品单价", "药品数量", "单品总价"], encoding=sys.stdout.encoding)
            for row in results:
                table.add_row(row)
            print(table)
            cursor.execute("SELECT sum(total_price) FROM drugs_pay_view WHERE patient_no = '%s'" % pno)
            results = cursor.fetchall()
            print("--诊断总价：%s" % str(results)[2:-4])

        cursor.execute(
            "SELECT bed_price, nurse_price, DATE FROM host_pay_view WHERE patient_no =  '%s'" % pno)
        results = cursor.fetchall()
        if results:
            table = PrettyTable(["床位价格", "护理价格", "入院时间"], encoding=sys.stdout.encoding)
            for row in results:
                table.add_row(row)
            print(table)
            cursor.execute("SELECT (host_pay_view.bed_price + nurse_price) * TimeStampDiff(DAY, host_pay_view.DATE, curdate()) AS host_price FROM host_pay_view WHERE patient_no = '%s'" % pno)
            results = cursor.fetchall()
            print("--住院总价：%s" % str(results)[2:-4])
        else:
            print("--查无记录")

    except Exception as error:
        print(error)
    finally:
        cursor.close()
        conn.close()
    pass



def showTable(table_name):
    conn = connect_init()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM %s" % table_name)
        results = cursor.fetchall()
        table = PrettyTable(DataDictionary.title_dict[table_name], encoding=sys.stdout.encoding)
        for row in results:
            table.add_row(row)
        print(table)
    except Exception as error:
        err_str = DataDictionary.error_dict[str(error)[1:5]]
        if err_str:
            print(err_str)
        else:
            print("--【警告】 查询失败，系统错误：\n", error)
            print(error)
    finally:
        cursor.close()
        conn.close()