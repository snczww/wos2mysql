# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 15:51:32 2017

@author: zww
任务需求，把mysql的wos数据读取，然后使用spacy分词在写会数据库用,分割
"""

import pymysql
import spacy

def query_data():
    db = pymysql.connect('localhost', 'root', '890', 'zls', charset='utf8')
    cursor = db.cursor()
    sql='SELECT AB FROM xiangmudata'
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        #print(results)
        #print(sql)
    
    except Exception as e:
        print('数据库读取异常', e)
    db.close()
    return results
def update_to_sql (AB,FC):   
    db = pymysql.connect('localhost', 'root', '890', 'zls', charset='utf8')
    cursor = db.cursor()
    sql='UPDATE xiangmudata SET FC="%s" WHERE AB="%s"' % (FC,AB)
    try:
        cursor.execute(sql)
        db.commit()
        print('插入数据成功')
    
    except Exception as e:
        print('插入数据异常', e)
        db.close()


def get_FC(text):
    s=''
    b= nlp(text)
    for np in b.noun_chunks:
        #print(np)
        s=s+str(np)+','
    return s      
        
nlp=spacy.load('en')
results=query_data()
F = open("tmp.txt", "w") 
for i in range(len(results)):
    t=str(results[i]).replace('\'', '').strip('()"')
    print(t[:-1])
    print('')
    FC=get_FC(t)
    print(FC)
    print('')
    F.write(t[:-1] + "\n")
    F.write(FC + "\n")
    update_to_sql (t[:-1].strip('\\'),FC)