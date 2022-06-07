# -*- coding = utf-8 -*-
# @Time : 2022/5/6 19:29
# @Author : Architect
# @File : dataOperator.py
# @Software : PyCharm


import sys
from datetime import date

from prettytable import PrettyTable
from dataDictionary import DataDictionary
from dbConnector import connect_init
from pymysql.err import IntegrityError


def updateData(data_tuple):
    conn = connect_init()
    cursor = conn.cursor()
    try:
        print("UPDATE %s SET %s = '%s' WHERE %s = '%s';" % data_tuple)
        cursor.execute("UPDATE %s SET %s = '%s' WHERE %s = '%s';" % data_tuple)
        conn.commit()
        print("--成功在 %s 数据表更新数据" % data_tuple[0])
    except IntegrityError as error:
        err_str = DataDictionary.error_dict[str(error)[1:5]]
        if err_str:
            print(err_str)
        else:
            print("--【警告】 信息删除失败，系统错误：\n", error)
            print(error)
    finally:
        cursor.close()
        conn.close()

def deleteData(data_tuple):
    conn = connect_init()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM %s WHERE %s = '%s';"% data_tuple)
        conn.commit()
        print("--成功在 %s 数据表删除数据" % data_tuple[0])
    except IntegrityError as error:
        err_str = DataDictionary.error_dict[str(error)[1:5]]
        if err_str:
            print(err_str)
        else:
            print("--【警告】 信息删除失败，系统错误：\n", error)
            print(error)
    finally:
        cursor.close()
        conn.close()


def addData(table_name, data_tuple):
    conn = connect_init()
    cursor = conn.cursor()
    try:
        cursor.execute(DataDictionary.format_dict[table_name] % data_tuple)
        conn.commit()
        print("--成功插入数据信息到 %s 数据表" % table_name)
    except IntegrityError as error:
        err_str = DataDictionary.error_dict[str(error)[1:5]]
        if err_str:
            print(err_str)
        else:
            print("--【警告】 信息插入失败，系统错误：\n", error)
            print(error)
    finally:
        cursor.close()
        conn.close()


def addPatient():
    table_name = "patients"
    column_name = "pno"
    capital = "P"
    num_len = 4
    pno = inputNum("> --编号（按ENTER自动填写）：", capital, num_len, necessary=False)
    pname = inputStr("> --姓名（必填）：", necessary=True)
    psex = inputStr("> --性别（男/女）：", range=["男", "女"], necessary=True)
    pbirth = inputNum("> --出生年份：", num_len=4, necessary=True)
    paddress = inputStr("> --住址：", necessary=False)
    pdate = inputDate("> --入院时间（yyyy-mm-dd）：", necessary=False)
    if pno == "":
        pno = getDefaultNum(table_name, column_name, capital, num_len)

    pbirth = int(pbirth)
    addData(table_name, (pno, pname, psex, pbirth, paddress, pdate[0], pdate[1], pdate[2]))


def addDoctor():
    table_name = "doctors"
    column_name = "dno"
    capital = "D"
    num_len = 4
    dno = inputNum("> --编号（按ENTER自动填写）：", capital, num_len, necessary=False)
    dname = inputStr("> --姓名（必填）：", necessary=True)
    dsex = inputStr("> --性别（男/女）：", range=["男", "女"], necessary=True)
    dbirth = inputNum("> --出生年份：", num_len=4, necessary=True)
    ddept = inputStr("> --科室：", necessary=False)
    dlevel = inputStr("> --职称：", necessary=False)
    if dno == "":
        dno = getDefaultNum(table_name, column_name, capital, num_len)

    dbirth = int(dbirth)
    addData(table_name, (dno, dname, dsex, dbirth, ddept, dlevel))


def addNurse():
    table_name = "nurses"
    column_name = "nno"
    capital = "n"
    num_len = 4
    nno = inputNum("> --编号（按ENTER自动填写）：", capital, num_len, necessary=False)
    nname = inputStr("> --姓名（必填）：", necessary=True)
    nsex = inputStr("> --性别（男/女）：", range=["男", "女"], necessary=True)
    nbirth = inputNum("> --出生年份：", num_len=4, necessary=True)
    ndept = inputStr("> --科室：", necessary=False)
    nlevel = inputStr("> --职称：", necessary=False)
    if nno == "":
        nno = getDefaultNum(table_name, column_name, capital, num_len)

    nbirth = int(nbirth)
    addData(table_name, (nno, nname, nsex, nbirth, ndept, nlevel))


def addBed():
    table_name = "beds"
    column_name = "bno"
    capital = "B"
    num_len = 4
    bno = inputNum("> --编号（按ENTER自动填写）：", capital, num_len, necessary=False)
    bprice = inputNum("> --床位价格（元/天）：", necessary=True)
    if bno == "":
        bno = getDefaultNum(table_name, column_name, capital, num_len)
    bprice = int(bprice)
    addData(table_name, (bno, bprice))


def addDrug():
    table_name = "drugs"
    column_name = "dno"
    capital = "M"
    num_len = 5
    dno = inputNum("> --编号（按ENTER自动填写）：", capital, num_len, necessary=False)
    dname = inputStr("> --药品学名（必填）：", necessary=True)
    dtype = inputStr("> --类型（中药/西药）：", range=["中药", "西药"], necessary=True)
    dprice = inputFloat("> --单价（元）：", necessary=True)
    dstorage = inputNum("> --库存：", necessary=True)
    if dno == "":
        dno = getDefaultNum(table_name, column_name, capital, num_len)

    dprice = float(dprice)
    dstorage = int(dstorage)
    addData(table_name, (dno, dname, dtype, dprice, dstorage))


def addDiagnose():
    table_name = "dp_rel"
    column_name = "dpno"
    capital = "DP"
    num_len = 5
    dpno = inputNum("> --编号（按ENTER自动填写）：", capital, num_len, necessary=False)
    dno = inputNum("> --医生编号：", "D", 4, necessary=True)
    pno = inputNum("> --患者编号：", "P", 4, necessary=True)
    illness = inputStr("> --诊断结果：", necessary=False)
    if dpno == "":
        dpno = getDefaultNum(table_name, column_name, capital, num_len)
    addData(table_name, (dpno, dno, pno, illness))


def addDrugSell():
    table_name = "drug_sell"
    column_name = "dsno"
    capital = "DS"
    num_len = 5
    dsno = inputNum("> --编号（按ENTER自动填写）：", capital, num_len, necessary=False)
    dpno = inputNum("> --诊断编号：", "DP", 5, necessary=True)
    dno = inputNum("> --药品编号：", "M", 5, necessary=True)
    dnum = inputNum("> --药品数量：", necessary=True)
    dnum = int(dnum)
    if dsno == "":
        dsno = getDefaultNum(table_name, column_name, capital, num_len)
    addData(table_name, (dsno, dno, dnum, dpno))


def addHost():
    table_name = "host_rel"
    column_name = "hno"
    capital = "H"
    num_len = 5
    hno = inputNum("> --编号（按ENTER自动填写）：", capital, num_len, necessary=False)
    nno = inputNum("> --护士编号：", "N", 4, necessary=True)
    pno = inputNum("> --病患编号：", "P", 4, necessary=True)
    bno = inputNum("> --床位编号：", "B", 4, necessary=True)
    hdate = inputDate("> --住院时间（yyyy-mm-dd）：", necessary=False)
    if hno == "":
        hno = getDefaultNum(table_name, column_name, capital, num_len)
    addData(table_name, (hno, nno, pno, bno, hdate[0], hdate[1], hdate[2]))


def inputNum(sentence, capital="", num_len=0, necessary=True):
    while True:
        no = input(sentence)
        cp_len = len(capital)
        if not necessary:
            if no == "":
                break
        if num_len == 0:
            if no[0:cp_len] == capital and is_int(no[cp_len:]):
                break
        else:
            if no[0:cp_len] == capital and len(no) == num_len + cp_len and is_int(no[cp_len:]):
                break
    return no


def inputFloat(sentence, necessary=True):
    while True:
        f = input(sentence)
        if not necessary:
            if f == "":
                break
        if is_float(f):
            break
    return f


def inputStr(sentence, range=None, necessary=False):
    while True:
        string = input(sentence)
        if range is None:
            if necessary:
                if string != "":
                    break
            else:
                break
        else:
            if necessary:
                if string != "" and (string in range):
                    break
            else:
                if string in range:
                    break
    return string


def inputDate(sentence, necessary=False):
    while True:
        d = input(sentence)
        if necessary:
            if d == "":
                return None
        dt = is_date(d)
        if dt is not None:
            return [int(dt.month), int(dt.day), int(dt.year)]


def is_date(datestr):
    try:
        d = date.fromisoformat(datestr)
        return d
    except ValueError:
        return None


def is_int(s):
    try:
        i = int(s)
        if i >= 0:
            return True
        else:
            return False
    except ValueError:
        return False


def is_float(s):
    try:
        i = float(s)
        return True
    except ValueError:
        return False


def getDefaultNum(table_name, column_name, capital, num_len):
    old_max = getMaxNum(table_name, column_name)
    return getNewNum(old_max, capital, num_len)


def getMaxNum(table_name, column_name):
    conn = connect_init()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT MAX(%s) FROM %s" % (column_name, table_name))
        results = cursor.fetchone()
        return str(results[0])
    except Exception as error:
        print(error)
    finally:
        cursor.close()
        conn.close()


def getNewNum(old_num, capital, num_len):
    cp_len = len(capital)
    num = int(old_num[cp_len:])
    num_bound = 10 ** num_len
    newNum = num + 1
    if newNum >= num_bound:
        return None
    else:
        return capital + str(newNum).zfill(num_len)
