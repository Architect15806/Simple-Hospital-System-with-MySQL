# -*- coding = utf-8 -*-
# @Time : 2022/5/6 22:51
# @Author : Architect
# @File : dataDictionary.py
# @Software : PyCharm

class DataDictionary(object):

    xlsx_path = "data.xlsx"

    format_dict = {
            'doctors': "INSERT INTO doctors VALUES ('%s', '%s', '%s', %d, '%s', '%s')",
            'nurses': "INSERT INTO nurses VALUES ('%s', '%s', '%s', %d, '%s', '%s')",
            'patients': "INSERT INTO patients VALUES ('%s', '%s', '%s', %d, '%s', STR_TO_DATE('%d-%d-%d', '%%m-%%d-%%Y'))",
            'beds': "INSERT INTO beds VALUES ('%s', %f)",
            'drugs': "INSERT INTO drugs VALUES ('%s', '%s', '%s', %f, %d)",
            'dp_rel': "INSERT INTO dp_rel VALUES ('%s', '%s', '%s', '%s')",
            'drug_sell': "INSERT INTO drug_sell VALUES ('%s', '%s', %d, '%s')",
            'host_rel': "INSERT INTO host_rel VALUES ('%s', '%s', '%s', '%s', STR_TO_DATE('%d-%d-%d', '%%m-%%d-%%Y'))",
        }
    title_dict = {
            'doctors': ['医生编号', '医生姓名', '医生性别', '医生生年', '医生科室', '医生职称'],
            'nurses': ['护士编号', '护士姓名', '护士性别', '护士生年', '护士科室', '护士职称'],
            'patients': ['病患编号', '病患姓名', '病患性别', '病患生年', '病患住址', '入院时间'],
            'beds': ['床位编号', '床位价格（元/天）'],
            'drugs': ['药品编号', '药品名称', '药品类型', '药品单价（元）', '药品当前库存（件）'],
            'dp_rel': ['诊断编号', '医生编号', '患者编号', '诊断结果'],
            'drug_sell': ['开药单号', '药品编号', '开药数量', '诊断编号'],
            'host_rel': ['住院编号', '护士编号', '病患编号', '床位编号', '住院起始日期'],
        }
    type_dict = {}
    error_dict = {
        '1146': "--【警告】 查无此表",
        '1452': "--【警告】 信息插入失败，请确保信息内容属于合理范畴"
    }
    info_dict = {
            '医者迁': ["doctors", "dno", "dlevel"],
            '护者迁': ["nurses", "nno", "nlevel"],
            '除痢': ["dp_rel", "dpno", "DP", 5],
            '处方': ["drug_sell", "dsno", "DS", 5],
            '卧寝': ["host_rel", "hno", "H", 4],
        }