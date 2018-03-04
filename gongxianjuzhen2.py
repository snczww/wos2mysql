#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/2 19:19
# @Author  : zww
# @Site    : 
# @File    : gongxianjuzhen2.py
# @Software: PyCharm

import xlrd

#读入表格数据,返回形如['/././','././','/././','/././']格式的列表
def readxls_bycol(path,colnum):
    xl = xlrd.open_workbook(path)
    table = xl.sheets()[0]
    data = list(table.col_values(colnum))
    print(data)
    print('----------1---------')
    return data

#处理表格数据, 返回无重复的所有出现过的关键词set
def deal_data(data):
    data_list = []
    data_set = set()
    for i in data:
         data_list.extend(i.split('/'))
#    data_list.sort()   #!!!高亮, 升序排列??????
    data_set=set(data_list)
    print(data_set)
    print('----------2---------')
    return data_set

#根据set,可建立一个二维列表,并填充其其一行以及第一列, 返回建好框架的二维列表
def creat_list_2d(data_set):
    i = len(data_set)+1
    #list1=[['' for x in range(i)] for y in range(i)]
    list_2d = [[0 for col in range(i)] for row in range(i)]  #建一个空二维列表的方法噢~
    n=1
    for row_1 in data_set:
        list_2d[0][n] = row_1   #填充第一行数据
        n+=1
        if n == i:
            break
    print(list_2d)
    m=1
    print(data_set)
    for cols in data_set:    #填充第一列数据
        list_2d[m][0] = cols
        m += 1
        if m == i:
            break
    print(list_2d)
    print('----------3---------')
    return list_2d


#计算共现次数, 填充二维列表~  返回填好的列表~
def count_data(list_2d,data,data_set):
    data_formted= []
    for i in data:
        data_formted.append(i.split('/'))
    print(data_formted)
    print('----------4---------')
    for row in range(1,len(data_set)):
        for col in range(1,len(data_set)):
            if row == col:
                continue
            else:
                counter = 0
                for i in data_formted:
                    if list_2d[col][0] in i and list_2d[0][row] in i :
                        counter += 1
                list_2d[row][col] = counter
    print(list_2d)
    print('----------5---------')
    return list_2d

#把矩阵写进txt~~~~

def putdata_intotxt(path,matrix):
    with open(path,'w') as f :
        for row in range(0,len(matrix)):
            for col in range(0,len(matrix)):#二维列表中的每一个元素都走一遍
                f.write(str(matrix[row][col]) + '\t')  #因为write()只接字符串类型啊
            f.write('\n')

def main():
    path_xls = r'outt.xlsx'     #---测试数据---
    path_txt= r'共现矩阵.txt'    #---测试数据---
    colnum = 0
    data = readxls_bycol(path_xls,colnum)
    data_set = deal_data(data)
    list_2d = creat_list_2d(data_set)
    matrix = count_data(list_2d,data,data_set)
    print(matrix)
    putdata_intotxt(path_txt,matrix)


if __name__=='__main__':
    main()
    print('你的文件夹多了一个共现矩阵的结果~快去看看吧XP')
