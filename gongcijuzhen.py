#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/2 16:54
# @Author  : zww
# @Site    : 
# @File    : gongcijuzhen.py
# @Software: PyCharm
import numpy as np
from reader import *
import time
from pprint import pprint as p


def log(func):
    def wrapper(*args, **kwargs):
        now_time = str(time.strftime('%Y-%m-%d %X', time.localtime()))
        print('------------------------------------------------')
        print('%s %s called' % (now_time, func.__name__))
        print('Document:%s' % func.__doc__)
        print('%s returns:' % func.__name__)
        re = func(*args, **kwargs)
        p(re)
        return re
    return wrapper

@log
def get_dict(data):
    formated_data = []
    for ech in data:
        ech_line = ech.split('/')
        formated_data.append(ech_line)

    originlines = []
    dict1 = {}
    for row in formated_data:
        originlines.append(row)
        for word in row:
            if word != '':
                if word in dict1:
                    dict1[word] += 1
                else:
                    dict1[word] = 1
    return dict1


@log
def get_set_key(dic,threshold):
    '''选取频数大于等于Threshold的关键词构建一个集合，用于作为共现矩阵的首行和首列'''
    wf = {k: v for k, v in dic.items() if v >= threshold}
    set_key_list=[]
    for a in sorted(wf.items(), key=lambda item: item[1], reverse=True):
        set_key_list.append(a[0])
    return set_key_list


@log
def format_data(data,set_key_list):
    '''格式化需要计算的数据，将原始数据格式转换成二维数组'''
    formated_data = []
    for ech in data:
        ech_line = ech.split('/')

        temp=[]            # 筛选出format_data中属于关键词集合的词
        for e in ech_line:
            if e in set_key_list:
                temp.append(e)
        ech_line=temp

        ech_line = list(set(filter(lambda x: x != '', ech_line))) #set去掉重复数据
        formated_data.append(ech_line)
    return formated_data


@log
def build_matirx(set_key_list):
    '''建立矩阵，矩阵的高度和宽度为关键词集合的长度+1'''
    edge = len(set_key_list)+1
    # matrix = np.zeros((edge, edge), dtype=str)
    matrix = [['' for j in range(edge)] for i in range(edge)]
    return matrix


@log
def init_matrix(set_key_list, matrix):
    '''初始化矩阵，将关键词集合赋值给第一列和第二列'''
    matrix[0][1:] = np.array(set_key_list)
    matrix = list(map(list, zip(*matrix)))
    matrix[0][1:] = np.array(set_key_list)
    return matrix


@log
def count_matrix(matrix, formated_data):
    '''计算各个关键词共现次数'''
    keywordlist=matrix[0][1:]  #列出所有关键词
    appeardict={}  #每个关键词与 [出现在的行(formated_data)的list] 组成的dictionary
    for w in keywordlist:
        appearlist=[]
        i=0
        for each_line in formated_data:
            if w in each_line:
                appearlist.append(i)
            i +=1
        appeardict[w]=appearlist
    for row in range(1, len(matrix)):
        # 遍历矩阵第一行，跳过下标为0的元素
        for col in range(1, len(matrix)):
                # 遍历矩阵第一列，跳过下标为0的元素
                # 实际上就是为了跳过matrix中下标为[0][0]的元素，因为[0][0]为空，不为关键词
            if col >= row:
                #仅计算上半个矩阵
                if matrix[0][row] == matrix[col][0]:
                    # 如果取出的行关键词和取出的列关键词相同，则其对应的共现次数为0，即矩阵对角线为0
                    matrix[col][row] = str(0)
                else:
                    counter = len(set(appeardict[matrix[0][row]])&set(appeardict[matrix[col][0]]))

                    matrix[col][row] = str(counter)
            else:
                matrix[col][row]=matrix[row][col]
    return matrix

def putdata_intotxt(path,matrix):
    with open(path,'w') as f :
        for row in range(0,len(matrix)):
            for col in range(0,len(matrix)):#二维列表中的每一个元素都走一遍
                f.write(str(matrix[row][col]) + '\t')  #因为write()只接字符串类型啊
            f.write('\n')

def main():
    keyword_path = r'outt.xlsx'
    output_path = r'2zl共现矩阵.txt'
    data = readxls_col(keyword_path)[0]
    dict1=get_dict(data)
    set_key_list = get_set_key(dict1,2)
    formated_data = format_data(data,set_key_list)
    matrix = build_matirx(set_key_list)
    matrix = init_matrix(set_key_list, matrix)
    result_matrix = count_matrix(matrix, formated_data)
    putdata_intotxt(output_path, result_matrix)
    #np.savetxt(output_path, result_matrix, fmt=('%s,'*len(matrix))[:-1])

if __name__ == '__main__':
    main()