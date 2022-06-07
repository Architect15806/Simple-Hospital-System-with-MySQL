# -*- coding = utf-8 -*-
# @Time : 2022/5/6 19:18
# @Author : Architect
# @File : dataReader.py
# @Software : PyCharm
import xlrd

from dataDictionary import DataDictionary


class DataReaderIter(object):
    def __init__(self, sheet_name):
        self.data = xlrd.open_workbook(DataDictionary.xlsx_path)
        self.sheet = self.data.sheet_by_name(sheet_name)  # 设定为医生表
        self.row_num = 2  # 起始行号-1，前两行是表头和数据类型，第三行开始
        self.data_type = self.sheet.row_values(1)
        self.rows = self.sheet.nrows  # 行数
        # DataDictionary.title_dict[sheet_name] = self.sheet.row_values(0)
        DataDictionary.type_dict[sheet_name] = self.sheet.row_values(1)

    def __iter__(self):
        return self

    def __next__(self):
        if self.row_num < self.rows:
            row_data = self.standardize(self.sheet.row_values(self.row_num))
            self.row_num += 1
            return row_data
        else:
            raise StopIteration

    def standardize(self, target):
        res = []
        for (tp, tg) in zip(self.data_type, target):
            if tp == "varchar":
                res.append(str(tg))
            elif tp == "int":
                res.append(int(tg))
            elif tp == "double":
                res.append(float(tg))
        return tuple(res)