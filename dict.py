# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 11:11:29 2018

@author: zww
替换
"""
 
import pandas as pd
df = pd.read_csv(r'D:\sourcecode\zhaolaoshi\dict.csv') 
f=open(r'D:\sourcecode\zhaolaoshi\zldict.csv')
out=open('D:\out.txt','w')
fr=f.read()
fr=fr.lower()
hu=fr
for i in range(len(df)):
    hu=hu.replace(r';'+df.ix[i]['b']+r';',r';'+str(df.ix[i]['a'])+r';')
    #print(fr)
out.write(hu)
out.close()
