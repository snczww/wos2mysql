#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/2 20:00
# @Author  : zww
# @Site    : 
# @File    : gongxianjuzhen3chinese.py
# @Software: PyCharm
import os
import xlrd
import re
from pprint import pprint as pt


def readxls(path):
    xl = xlrd.open_workbook(path)
    sheet = xl.sheets()[0]
    data = []
    for i in range(0, sheet.ncols):
        data.append(list(sheet.col_values(i)))
    return (data[0])


def wryer(path, text):
    with open(path, 'a', encoding='utf-8') as f:
        f.write(text)
    return path+' is ok!'


def buildmatrix(x, y):
    return [[0 for j in range(y)] for i in range(x)]


def dic(xlspath):
    keygroup = readxls(xlspath)
    keytxt = '/'.join(keygroup)
    keyfir = keytxt.split('/')
    keylist = list(set([key for key in keytxt.split('/') if key != '']))
    keydic = {}
    pos = 0
    for i in keylist:
        pos = pos+1
        keydic[pos] = str(i)
    return keydic


def showmatrix(matrix):
    matrixtxt = ''
    count = 0
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            matrixtxt = matrixtxt+str(matrix[i][j])+'\t'
        matrixtxt = matrixtxt[:-1]+'\n'
        count = count+1
        print('No.'+str(count)+' had been done!')
    return matrixtxt


def inimatrix(matrix, dic, length):
    matrix[0][0] = '+'
    for i in range(1, length):
        matrix[0][i] = dic[i]
    for i in range(1, length):
        matrix[i][0] = dic[i]
    # pt(matrix)
    return matrix


def countmatirx(matrix, dic, mlength, keylis):
    for i in range(1, mlength):
        for j in range(1, mlength):
            count = 0
            for k in keylis:
                ech = str(k).split('/')
                # print(ech)
                if str(matrix[0][i]) in ech and str(matrix[j][0]) in ech and str(matrix[0][i]) != str(matrix[j][0]):
                    count = count+1
                else:
                    continue
            matrix[i][j] = str(count)
    return matrix


def main():
    xlspath = r'test.xlsx'
    wrypath = r'1.txt'
    keylis = (readxls(xlspath))
    keydic = dic(xlspath)
    length = len(keydic)+1
    matrix = buildmatrix(length, length)
    print('Matrix had been built successfully!')
    matrix = inimatrix(matrix, keydic, length)
    print('Col and row had been writen!')
    matrix = countmatirx(matrix, keydic, length, keylis)
    print('Matrix had been counted successfully!')
    matrixtxt = showmatrix(matrix)
    # pt(matrix)
    print(wryer(wrypath, matrixtxt))
    # print(keylis)

if __name__ == '__main__':
    main()