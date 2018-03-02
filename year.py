# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 21:51:43 2018

@author: zww
"""

import numpy as np
import pandas as pd

yuan = pd.read_csv('zlyear.csv',delimiter=',')
word = pd.read_csv('zlwords.csv',delimiter=',')
for i in range(len(word)):
    print(i)
    m=''
    for j in range(len(yuan)):
        #print(j)
        s=yuan.ix[j,['1']].values[0]
        s=s.lower()
        word1=';'+word.ix[i,['w']].values[0]+';'
        if word1 in s:
            m+=str(yuan.ix[j,['y']].values[0])
            m+=','
           
    word.ix[i,['y']]=m
    print(m)
word.to_csv('zlyyear12.csv')