# -*- coding = utf-8 -*-
# @Time : 2022/4/23 10:20
# @Author : Architect
# @File : hospital.py
# @Software : PyCharm
import dataDictionary
import dataInitiator as di
from dataOperator import *
from dataSearcher import showPayCheck, showTable

command_status = 0

command_status_list = [
    "",
    "$$ 诊疗 ",
    "$$ 人事 ",
    "$$ 资源 ",
]


def command_sys():
    global command_status
    while True:
        print("就绪 " + command_status_list[command_status] + "> ", end="")
        command = (input()).strip()

        if command_super(command):
            continue
        if command_status == 1:
            if command_medic_action(command):
                continue
        elif command_status == 2:
            if command_personnel_action(command):
                continue
        print("--查无此令，望三思而后行")


def command_super(command):
    global command_status
    if command == "返":
        command_status = 0
        return True
    elif command == "疗":
        command_status = 1
        return True
    elif command == "吏":
        command_status = 2
        return True
    elif command == "械":
        command_status = 3
        return True
    elif command[0:1] == "阅":
        if command.find('--') != -1:
            table_name = command.split('--')[1]
            showTable(table_name)
        else:
            print("--此令：【阅 --表名】")
        return True
    elif command[0:1] == "去":
        if command.find('--') != -1:
            try:
                operate = command.split('--')[1].strip()
                num = command.split('--')[2].strip()
                info_list = DataDictionary.info_dict[operate]
                deleteData((info_list[0], info_list[1], num))
            except KeyError as error:
                print("--此令：【去 --操作 --序号】")
        else:
            print("--此令：【去 --操作 --序号】")
        return True
    else:
        return False


def command_medic_action(command):
    if command == "抱恙":
        addPatient()
        return True
    elif command == "除痢":
        addDiagnose()
        return True
    elif command == "处方":
        addDrugSell()
        return True
    elif command == "卧寝":
        addHost()
        return True
    elif command[0:2] == "查账":
        if command.find('--') != -1:
            pno = command.split('--')[1]
            if len(pno) == 5 and pno[0:1] == 'P' and is_int(pno[1:]):
                showPayCheck(pno)
            else:
                print("--此令：【查账 --患者编号】，患者编号有误")
        else:
            print("--此令：【查账 --患者编号】")
        return True
    else:
        return False


def command_personnel_action(command):
    if command[0:3] == "医者迁":
        if command.find('--') != -1:
            try:
                num = command.split('--')[1].strip()
                level = command.split('--')[2].strip()
                info_list = DataDictionary.info_dict["医者迁"]
                updateData((info_list[0], info_list[2], level, info_list[1], num))
            except KeyError as error:
                print("--此令：【医者迁 --序号 --职级】")
        else:
            print("--此令：【医者迁 --序号 --职级】")
        return True
    elif command[0:3] == "护者迁":
        if command.find('--') != -1:
            try:
                num = command.split('--')[1].strip()
                level = command.split('--')[2].strip()
                info_list = DataDictionary.info_dict["护者迁"]
                updateData((info_list[0], info_list[2], level, info_list[1], num))
            except KeyError as error:
                print("--此令：【护者迁 --序号 --职级】")
        else:
            print("--此令：【护者迁 --序号 --职级】")
        return True
    pass


if __name__ == '__main__':
    di.db_init()
    command_sys()
    # addData('doctors', ('D0021', '张仲景', '男', 1701, '外科', '主任医师'))  # 正确的插入
    # addData('doctors', ('D0021', '张仲景', '男', 1701, '外科', '主医师'))  # 错误的插入
    # showTable('patients')
    # addPatient()
    # addDoctor()
    # addNurse()
    # addDrug()
    # addDiagnose()
    # addDrugSell()
    # addHost()
