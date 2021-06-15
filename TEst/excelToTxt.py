#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
Created on 2019��8��1��

@author: xuzhiyun
'''
import xlrd

'''
excel  change txt file
'''

def row2str(row_data):
    values = ""
    for i in range(len(row_data)):
        if i == len(row_data):
            values = values + str(row_data[i]) + "\t"
        else:
            values = values + str(row_data[i]) + "\t"
    return values


# 打开文件
try:
    data = xlrd.open_workbook("360white.xlsx")
except:
    print("fail to open file")
else:
    # 文件读写方式是追加
    file = open("360white.txt", "a", encoding='utf-8')
    # 表头
    table = data.sheets()[0]
    # 行数
    row_cnt = table.nrows
    # 列数
    col_cnt = table.ncols
    # 第一行数据
#     title = table.row_values(0)
    # 打印出行数列数
#     print(row_cnt)
#     print(col_cnt)
#     print(title)
    for j in range(1, row_cnt):
        row = table.row_values(j)
        # 调用函数，将行数据拼接成字符串
        row_values = row2str(row)
        # 将字符串写入新文件
        file.write(row_values + "\n")
    # 关闭写入的文件
    file.close()