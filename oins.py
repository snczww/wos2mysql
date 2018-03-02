# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 10:34:02 2017

@author: zww
"""
import pandas as pd
import csv

list1 = csv.reader(open('papm.csv', encoding='utf-8'))
ss='sjafhkldaghiudkshafkjdshfai'
for i in range(8):
    i=str(i).replace(" ","_")
    print('\n')
    print(str(i))
    for j in range(9):
        print (ss[j])

'''
out = open('out.csv', 'w', newline='')
csv_writer = csv.writer(out, dialect='excel')
csv_writer.writerow(list) '''



'''dataframe = pd.DataFrame({'a_name':data})
dataframe.to_csv("test.csv",index=False,sep='')'''